section .text
global _start

; -------------------------------------------
; PUSH INTO STACK MACROS
%macro pushd 0
    push rax
    push rbx
    push rcx
    push rdx
%endmacro
; -------------------------------------------



; -------------------------------------------
; POP FROM STACK MACROS
%macro popd 0
    pop rdx
    pop rcx
    pop rbx
    pop rax
%endmacro
; -------------------------------------------



; -------------------------------------------
; PRINT MESSAGE MACROS
%macro print 2
    pushd
    mov rax, 1
    mov rdi, 1
    mov rsi, %1             ; message
    mov rdx, %2             ; len of message
    syscall
    popd
%endmacro
; -------------------------------------------



; -------------------------------------------
; PRINT DIGIT NUMBER MACROS
%macro dprint 0
    pushd

    mov rbx, 0
    mov rcx, 10

    %%divide:
        xor rdx, rdx
        div rcx
        push rdx
        inc rbx                 ; increment

        cmp rax, 0
        jne %%divide

    %%digit:
        pop rax
        add rax, '0'
        mov [result], rax
        print result, 1
        dec rbx

        cmp rbx, 0
        jg %%digit

    popd
%endmacro
; -------------------------------------------



_start:
    mov rax, 0
    mov rbx, 0                      ; index

    jmp check_lens

print_x:
    mov eax, [x + 4*rbx]
    dprint
    print space, slen

    inc rbx
    cmp rbx, x_len
    jne print_x

    mov rbx, 0
    print newline, nlen
    jmp print_y

print_y:
    mov eax, [y + 4*rbx]
    dprint
    print space, slen

    inc rbx
    cmp rbx, y_len
    jne print_y

    jmp check_lens


; --------------------------------------------------
; Checking lengths of arrays
check_lens:
    mov eax, x_len
    mov ebx, y_len

    cmp eax, ebx
    jne print_not_equal

    mov rax, 0
    mov rbx, 0
    jmp sum

print_not_equal:
    print not_equal_message, len_not_equal
    jmp end
; --------------------------------------------------

sum:
    add eax, [x + 4*rbx]                        ; add rax x[rbx]
    sub eax, [y + 4*rbx]                        ; subtract rax y[rbx]

    inc rbx
    cmp rbx, x_len                              ; while rbx != x_len
    jne sum

    print average_message, len_average
    jmp print_minus

print_minus:
    cmp eax, 0                                  ; if sum is less than 0, print minus
    jnl print_average
    print minus, mlen
    neg eax                                     ; invert sum

    jmp print_average

print_average:
    mov rcx, x_len
    div rcx                                     ; rax (sum) / rcx (x_len)
    dprint                                      ; print rax

    cmp rdx, 0                                  ; if average is int: end
    je print_done

    jmp print_point

print_point:
    print point, plen                           ; print point
    mov rbx, 0

    jmp print_frac

print_frac:
    mov rcx, 10
    mov rax, rdx                                ; old_rdx *= 10
    mul rcx

    mov rcx, x_len
    div rcx                                     ; 10*old_rdx // x_len

    dprint
    inc rbx

    cmp rdx, 0
    je print_done

    cmp rbx, 10
    jle print_frac

    jmp print_done

print_done:
    print newline, nlen
    print done_message, len_done

    jmp end

end:
    mov rax, 60
    xor rdi, rdi
    syscall

section .data
    x dd 5, 3, 1, 4
    x_len equ (($ - x)/4)
    y dd 0, 2, 1, -3
    y_len equ (($ - y)/4)
    
    ; Done message for end of program
    done_message db 'Done', 0xA, 0xD
    len_done equ $ - done_message

    ; Newline symbol
    newline db 0xA, 0xD
    nlen equ $ - newline

    ; Space symbol
	space db ' '
	slen equ $ - space

    ; Symbol minus
    minus db '-'
    mlen equ $ - minus

    ; Symbol point
    point db '.'
    plen equ $ - point

    ; Message lens of array are not equal
    not_equal_message db 'Lens of arrays are not equal', 0xA, 0xD
    len_not_equal equ $ - not_equal_message

    ; Message average
    average_message db 'Average of x-y = '
    len_average equ $ - average_message


section .bss
    result resb 1
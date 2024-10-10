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

    ; jmp print_x
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
    add eax, [x + 4*rbx]
    ; sub eax, [y + 4*rbx]

    dprint
    print newline, nlen

    inc rbx
    cmp rbx, x_len
    jne sum

    jmp print_average

print_average:
    dprint
    print newline, nlen

end:
    print newline, nlen
    print done_message, len_done

    mov rax, 60
    xor rdi, rdi
    syscall

section .data
    x dd 5, 3, 2, 6, 1, 7, 4
    y dd 0, 10, 1, 9, 2, 8, 5
    x_len equ (($ - x)/8)
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

    ; Message lens of array are not equal
    not_equal_message db 'Lens of array are not equal', 0xA, 0xD
    len_not_equal equ $ - not_equal_message


section .bss
    result resb 1
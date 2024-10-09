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
    jmp check_lens

check_lens:
    mov rbx, x_len
    add rbx, '0'
    mov [result], rbx
    print [result], 1
    print space, slen

    mov rbx, y_len
    add rbx, '0'
    mov [result], rbx
    print [result], 1
    print newline, nlen    

    ; mov rax, y_len
    ; cmp x_len, rax
    ; jne print_not_equal

    jmp end

print_not_equal:
    print not_equal_message, len_not_equal
    jmp end

end:
    print newline, nlen
    print done_message, len_done

    mov rax, 60
    xor rdi, rdi
    syscall

section .data
    x dd 5, 3, 2, 6, 1, 7, 4
    y dd 0, 10, 1, 9, 2, 8, 5
    x_len equ $ - x
    y_len equ $ - y
    
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
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
        inc rbx

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



; -------------------------------------------
; PRINT RATIONAL
%macro rprint 2
    pushd

    mov eax, dword [%1]
    dprint
    print slash, hlen
    mov eax, dword [%2]
    dprint

    popd
%endmacro
; -------------------------------------------




_start:
    mov eax, dword [number]
    mov dword [x_num], eax
    mov dword [x_den], dword 2

    jmp calc_y

calc_x:
    mov eax, dword [y_num]
    mov dword [x_num], eax
    mov eax, dword [y_den]
    mov dword [x_den], eax

    jmp calc_y

calc_y:
    mov eax, dword [number]
    mul dword [x_den]
    mul dword [x_den]
    mov ebx, eax

    mov eax, dword [x_num]
    mul dword [x_num]
    add eax, ebx
    mov dword [y_num], eax

    mov eax, dword [x_num]
    mul dword [x_den]
    mov ecx, dword 2
    mul ecx
    mov dword [y_den], eax

    ;rprint y_num, y_den
    ;print arrow, alen

    jmp simple_y

simple_y:
    mov eax, dword [y_num]
    div dword [y_den]
    mov dword [y_num], eax
    mov dword [y_den], dword 1

    jmp compare

compare:
    mov eax, dword [y_num]
    mul dword [x_den]
    mov ebx, eax

    mov eax, dword [x_num]
    sub eax, ebx

    ;rprint y_num, y_den
    ;print newline, nlen

    cmp eax, dword [x_den]
    jge calc_x

    jmp print_done

print_done:
    mov eax, dword [y_num]
    dprint

    print newline, nlen
    print done_message, len_done

    jmp end

end:    
    mov rax, 60
    xor rdi, rdi
    syscall


section .data
    number dd 10000

    ; Newline symbol
    newline db 0xA, 0xD
    nlen equ $ - newline

    ; Space symbol
	space db ' '
	slen equ $ - space

    ; Symbol point
    point db '.'
    plen equ $ - point

    ; Symbol slash
    slash db '/'
    hlen equ $ - slash

    ; Arrow
    arrow db ' --> '
    alen equ $ - arrow

    ; Done message for end of program
    done_message db 'Done', 0xA, 0xD
    len_done equ $ - done_message


section .bss
    result resd 1
    x_num resd 1
    x_den resd 1
    y_num resd 1
    y_den resd 1

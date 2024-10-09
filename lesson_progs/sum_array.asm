%macro pushd 0
        push rax
        push rbx
        push rcx
        push rdx
%endmacro

%macro popd 0
        pop rdx
        pop rcx
        pop rbx
        pop rax
%endmacro

%macro print 2
        pushd
        mov rax, 1
        mov rdi, 1
        mov rsi, %1
        mov rdx, %2
        syscall
        popd
%endmacro

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

section .text
global _start

_start:
	mov rbx, 0                      ; index
	mov rcx, 0			; sum of array
        jmp range

range:
	push rbx
	add rbx, '0'
	mov [result], rbx
	print result, 1
	print space, slen
	pop rbx	

	mov al, [array+rbx]
	dprint
	print newline, nlen

	add cl, al

	inc rbx
	cmp rbx, arr_len
	jne range

	jmp end

end:
	print message_out, mlen
	mov rax, rcx
	dprint

	print newline, nlen
        print done, len
        print newline, nlen
        mov rax, 60
        xor rdi, rdi
        syscall

section .data
        array db 10, 13, 14, 7, 8, 12, 32, 54, 65, 3
	arr_len equ $ - array
	message_out db 'Sum = '
	mlen equ $ - message_out

        done db 'Done', 0xA, 0xD
        len equ $ - done
        newline db 0xA, 0xD
        nlen equ $ - newline
	space db ' '
	slen equ $ - space

section .bss
        result resb 1

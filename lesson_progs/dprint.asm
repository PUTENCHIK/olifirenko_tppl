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
	mov rax, [value]
	dprint
;	mov rcx, 10		; needed for dividing
;	mov rax, [value]	; a number for output
;	mov rbx, 0		; counter of digits

	print newline, nlen
	print done, len
	print newline, nlen
	mov rax, 60
	xor rdi, rdi
	syscall
	

section .data
	value dq 34535
	done db 'Done', 0xA, 0xD
	len equ $ - done
	newline db 0xA, 0xD
	nlen equ $ - newline

section .bss
	result resb 1

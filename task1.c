/*
 * Ross Stanga
 * Progamming Assignment 1
 * Student ID - 2549819
 */
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h> 
#include <signal.h>

void forkHomework() {

 int n, status;
 pid_t pid;
 printf("Enter a number: \n");
 scanf("%d",&n);
 FILE * fp = NULL;
 printf("You entered: %d\n\n", n);
 fp = fopen("task1Output5.txt", "w");

 for (int i = 0; i < n; i++) {
 	pid = fork();
 	if (pid == 0) {
    	printf("This is a child process. My pid = %d and my parent's id = %d.\n", getpid(),getppid());
    	fprintf(fp, "This is a child process. My pid = %d and my parent's id = %d.\n", getpid(),getppid());
		}

 	else if (pid > 0) {
    	printf("This is a parent process. My pid = %d and my parent's id = %d.\n", getpid(), getppid());
    	fprintf(fp, "This is a parent process. My pid = %d and my parent's id = %d.\n", getpid(), getppid());
    	puts("Waiting for my child to complete.\n");
    	wait(NULL);
    	
    	if (wait(&status) == -1) {
       		perror("wait() error");   
    		}
		}

	}

}

int main() {

    forkHomework();

}
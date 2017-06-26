#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdlib.h>

#define ZOMBIE 1
#define DEAD 1
#define ALIVE 0

/**
 * walking_dead - creates zombie process
 * Return: pid, either parent or child
 */
pid_t walking_dead(void)
{
	pid_t walker;

	walker = fork();

	if (walker)
	{
		printf("Zombie process created, PID: %d\n", walker);
		return (walker);
	}

	return (ALIVE);
}

/**
 * main - main function for zombie creation program
 * Return: 0 alwayss sucess!
 */
int main(void)
{
	int i, zombies;
	pid_t walker;

	zombies = 5;

	for (i = 0; i < zombies; i++)
	{
		walker = walking_dead();

		if (walker == ALIVE)
			exit(ALIVE);
	}
	pause();

	return (ALIVE);
}

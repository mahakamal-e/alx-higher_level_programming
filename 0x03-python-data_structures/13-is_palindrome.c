#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - function that used to check is palindrome
 * A palindrome is a sequence of elements that reads
 * the same forwards as backward
 *
 * @head: head of linkedlist
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp;
	int size_ = 0;
	int *link_el;
	int i;

	temp = *head;

	if (!(*head) || !head)
		return (1);
	while (temp )
	{
		size_++;
		temp = temp->next;
	}
	link_el = (int *)malloc(sizeof(int) * size_);
	if (link_el == NULL)
		return (0);
	temp = *head;
	for (i = 0; i < size_; i++)
	{
		link_el[i] = temp->n;
		temp = temp->next;
	}
	for (i = 0; i < size_ / 2; i++)
	{
		if (link_el[i] != link_el[size_ - i - 1])
		{
			free(link_el);
			return (0);
		}
	}
	free(link_el);
	return (1);
}



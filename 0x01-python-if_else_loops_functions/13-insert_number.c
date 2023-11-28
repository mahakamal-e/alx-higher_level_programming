#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - function used to inset node
 * @head: first element in node
 * @number: number that will be inserted
 * Return: the address of new node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *_tempNode = *head;
	listint_t *node_n;

	node_n = malloc(sizeof(listint_t));

	if (node_n == NULL)
		return (NULL);
	node_n->n = number;
	node_n->next = NULL;

	if (_tempNode == NULL)
	{
		node_n->next = _tempNode;
		return ((*head) = node_n);
	}
	if (_tempNode->n > node_n->n)
	{
		node_n->next = _tempNode;
		return ((*head) = node_n);
	}
	while (_tempNode)
	{
		if (!_tempNode->next || node_n->n < _tempNode->next->n)
		{
			node_n->next = _tempNode->next;
			_tempNode->next = node_n;
			return (_tempNode);
		}
		_tempNode = _tempNode->next;
	}
	return (NULL);

}

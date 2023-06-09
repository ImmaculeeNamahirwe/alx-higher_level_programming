#include "lists.h"

/**
 *insert_node - Adds a number to a singly-linked, sorted list.
 *@head: A pointer to the linked list's head
 *@number: The number to insert
 *
 *Return: NULL in case of failure
 *	a pointer to the new mode
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}


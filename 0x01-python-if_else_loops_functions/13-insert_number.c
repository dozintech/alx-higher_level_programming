#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a number into a given sorted singly-linked list
 * @head: The pointer to the head of the linked list
 * @number: The number to insert
 *
 * Return: The address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *cur_node = NULL, *node = NULL;

	if (head != NULL)
	{
		node = malloc(sizeof(listint_t));
		if (node != NULL)
		{
			node->n = number;
			cur_node = *head;
			while ((cur_node != NULL) && (cur_node->n < number))
			{
				if (((cur_node->next != NULL) && (cur_node->next->n < number)))
					cur_node = cur_node->next;
				else
					break;
			}
			if ((cur_node != NULL) && (cur_node->n < number))
			{
				node->next = cur_node->next;
				cur_node->next = node;
			}
			else
			{
				node->next = *head;
				*head = node;
			}
		}
	}
	return (node);
}

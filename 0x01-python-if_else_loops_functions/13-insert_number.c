#include "lists.h"
/**
 * insert_node - funtion add new node
 * @head: linked list
 * @number: num to add
 * Return: New linked list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = *head, *new_node;
	listint_t *n;
	int cont_pos = 0, cont;

	while (number > tmp->n)
	{
		cont_pos++;
		tmp = tmp->next;
	}
	tmp = *head;
	for (cont = 0; cont < cont_pos - 1; cont++)
		tmp = tmp->next;
	n = tmp->next;
	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;
	tmp->next = new_node;
	new_node->next = n;
	return (tmp);
}

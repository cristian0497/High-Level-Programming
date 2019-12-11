#include "lists.h"
/**
 *
 *
 *
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = *head, *new_node;
	listint_t *n;
	int cont_pos = 0, cont;

	while(number > tmp->n)
	{
/*		printf("->%d %d\n", cont_pos, tmp->n); */
		cont_pos++;
		tmp = tmp->next;
	}
	tmp = *head; //n
	for (cont = 0; cont < cont_pos - 1; cont++)
	{
		tmp = tmp->next;
	}
	n = tmp->next;
	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;
	tmp->next = new_node;
	new_node->next = n;

/*	printf(">>>%d %d\n", tmp->n ,cont_pos);*/
	return (tmp);
}

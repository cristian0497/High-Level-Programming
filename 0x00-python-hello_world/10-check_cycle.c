#include "lists.h"

/**
 * check_cycle - checl if linked list have cycle
 * @list: linked list pointer
 * Return: 1(Cycle) 0(NoCycle)
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp;

	tmp = list;
	while (tmp != NULL)
	{
		while (list != NULL)
		{
			if (tmp == list->next)
				return (1);
			list = list->next;
		}
		tmp = tmp->next;
	}
	return (0);
}

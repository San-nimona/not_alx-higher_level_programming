#include "lists.h"
/**
 * check_cycle - checks a linked list's cycle
 * @list: the linked list
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *temp;
	listint_t *prev;

	temp = list;
	prev = list;
	while (list && temp && temp->next)
	{
		list = list->next;
		temp = temp->next->next;

		if (list == temp)
		{
			list = prev;
			prev =  temp;
			while (1)
			{
				temp = prev;
				while (temp->next != list && temp->next != prev)
					temp = temp->next;

				if (temp->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}

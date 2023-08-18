#include "lists.h"
/**
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list->next;
	listint_t *slow = list;
	
	if (list == NULL)
		return 0;
	while (fast != NULL && fast->next != NULL && slow != NULL)
	{
		if (fast == slow)
			return 1;
		fast = fast->next->next;
		slow = slow->next;
	}
	return 0;
}

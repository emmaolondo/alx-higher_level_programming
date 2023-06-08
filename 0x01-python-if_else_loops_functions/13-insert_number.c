#include "lists.h"
/**
 * insert_node - a function in C that inserts a number into a sorted singly linked list.
 * @head: head pointer of the list
 * @number: number to be inserted
 *
 * Return: address of the new node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr, *new_ptr;

	ptr = *head;
	new_ptr = malloc(sizeof(listint_t));/*allocate memory to the new_ptr*/

	if (new_ptr == NULL)
		return (NULL);
	new_ptr->n = number;
	/* checck if the number at the head if greater than the new number
	 * if true let the new_ptr be the head pointer of the list
	 */
	if (ptr == NULL || ptr->n > number)
	{
		new_ptr->next = ptr;
		*head = new_ptr;
		return(new_ptr);
	}
	/* if the new number is greater than the number at a given pointer loop
	 * through the list*/
	while(ptr && ptr->next && ptr->next->n < number)
	{
		ptr = ptr->next;
	}
	new_ptr->next = ptr->next;
	ptr->next = new_ptr;
	return (new_ptr);
}

#include "lists.h"

/**
 * reverse_listint - reverses a singly-linked listint_t list
 * @head: pointer to the starting node of the list to reverse
 *
 * Return: pointer to head of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the linked list
 * 
 * Return: If the linked is a palindome 1 if not 0
 */
int is_palindrome(listint_t **head){
  listint_t *temp, *x, *y;
  size_t size = 0, i;

  if (*head == NULL || (*head)->next == NULL)
    return(1);

  temp = *head;
  while (temp)
    {
      size++;
      temp =temp->next;
    }

  temp =  *head;
  for (i =  0; i < (size / 2) - 1; i++)
    temp = temp->next;

  if ((size % 2) ==  0 && temp->n != temp->next->n)
    return(0);

  temp = temp->next->next;
  x =  reverselistint(&temp);
  y = x;
  temp = *head;
  while (x)
    {
      if (temp->n != rev->n)
	return (0);
      temp = temp->next;
      x = x->next;
    }
        reverse_listint(&y);

	return (1);
}

from queue import Queue
import time
import random


class Ticket:
   def __init__(self, ticket_number):
       self.ticket_number = ticket_number
       self.timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())

   def __repr__(self):
       return f"Ticket No: {self.ticket_number}, {self.timestamp}"


def create_ticket(sequence_number):
   return Ticket(sequence_number)


def issue_tickets(queue, number_of_tickets=1000):
   for current_ticket_number in range(1, number_of_tickets + 1):
       ticket = create_ticket(current_ticket_number)
       print(ticket)
       queue.put(ticket)
       time.sleep(random.uniform(0.5, 3))


def serve_tickets(queue):
   while not queue.empty():
       ticket = queue.get()
       print(f"{ticket.ticket_number}, Issued at: {ticket.timestamp}")
       time.sleep(random.uniform(1, 2))


ticket_queue = Queue()
issue_tickets(ticket_queue, 1000)
serve_tickets(ticket_queue)


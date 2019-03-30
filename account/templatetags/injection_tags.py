from django import template
from django.contrib.auth.models import Group
from django.db.models import Q
from ticket.models import Ticket
from itertools import chain

register = template.Library()


@register.filter(name='groups')
def groups(user):
    """
    Returns all groups the user is a member of.
    :param user: the logged-in user
    :return: Array of groups
    """
    try:
        my_groups = user.groups.all()
        return my_groups
    except Exception as e:
        print(e)


@register.filter(name='inbox')
def inbox(user):
    """
    Returns all newly assigned tickets that were either directly assigned to
    the user or to a group where the user is a member.
    :param user: the logged-in user
    :return: array of tickets
    """
    try:
        inbox_tickets = Ticket.objects.filter(assigned_user=user,
                                              accepted=False)
        my_groups = user.groups.all()
        group_tickets = Ticket.objects.filter(assigned_group__in=my_groups,
                                              assigned_user=None,
                                              accepted=False).exclude(
            ignored_by=user)
        result_list = reversed(sorted(
            chain(inbox_tickets, group_tickets),
            key=lambda instance: instance.time_assign_user))
        return result_list
    except Exception as e:
        print(e)


@register.filter(name='inbox_count')
def inbox_count(user):
    """
    Counts all newly assigned tickers that were either directly assigned to
    the user or to a group where the user is a member.
    :param user: the logged-in user
    :return: number of open tickets as integer
    """
    try:
        inbox_tickets_count = Ticket.objects.filter(assigned_user=user,
                                                    accepted=False).count()
        my_groups = user.groups.all()
        group_tickets = Ticket.objects.filter(assigned_group__in=my_groups,
                                              assigned_user=None,
                                              accepted=False).exclude(
            ignored_by=user).count()
        return inbox_tickets_count + group_tickets
    except Exception as e:
        print(e)


@register.filter(name='rejected_count')
def rejected_count(user):
    """
    Counts all rejected tickets of the user.
    :param user: the logged-in user
    :return: number of rejected tickets as integer
    """
    try:
        rejected_tickets_count = Ticket.objects.filter(
            Q(creator_user=user, assigned_user=None, rejected=True) | Q(
                dispatcher=user, assigned_user=None, rejected=True)).count()
        return rejected_tickets_count
    except Exception as e:
        print(e)

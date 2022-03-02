from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Meetup
from .forms import MeetupForm

def index(request):
    return render(request, 'index.html')
    
def meetups(request):
    meetups = Meetup.objects.all()
    context = {'meetups': meetups}
    return render(request, 'meetups/meetups.html', context)

def meetup(request, pk):
    meetupObj = Meetup.objects.get(id=pk)
    dog_sizes = meetupObj.dog_sizes.all()
    attendees = meetupObj.attendees.all()
    return render(request, 'meetups/meetup-details.html', {'meetup': meetupObj, 'dog_sizes': dog_sizes, 'attendees': attendees})

@login_required(login_url='login')
def create_meetup(request):
    profile = request.user.profile
    form = MeetupForm()


    if request.method == "POST":
        form = MeetupForm(request.POST, request.FILES)
        
        if form.is_valid():
            meetup = form.save()
            meetup.organizer = profile
            attendees = meetup.attendees
            attendees.add(profile)
            meetup.save()

            return redirect('meetups')

    context = {'form': form}
    return render(request, 'meetups/meetup-form.html', context)

@login_required(login_url='login')
def update_meetup(request, pk):
    profile = request.user.profile
    meetup = profile.meetup_set.get(id=pk)
    form = MeetupForm(instance=meetup)

    if request.method == "POST":
        form = MeetupForm(request.POST, request.FILES, instance=meetup)

        if form.is_valid():
            meetup = form.save()
            return redirect('meetups')

    context = {'form': form, 'meetup': meetup}
    return render(request, 'meetups/meetup-form.html', context)

@login_required(login_url='login')
def delete_meetup(request, pk):
    profile = request.user.profile
    meetup = profile.meetup_set.get(id=pk)

    if request.method == "POST":
        meetup.delete()
        return redirect('meetups')

    context = {'object': meetup}
    return render(request, 'delete-template.html', context)

@login_required(login_url='login')
def attend_meetup(request, pk):
    meetup = Meetup.objects.get(id=pk)
    attendee = request.user.profile
    attendees = meetup.attendees
    attendees.add(attendee)
    print(f'Attending: {meetup.attendees}')
    messages.success(request, 'You are now attending this meetup!')
    
    context = {'meetup': meetup}
    return render(request, 'meetups/meetup-details.html', context)

@login_required(login_url='login')
def cancel_attend_meetup(request, pk):
    meetup = Meetup.objects.get(id=pk)
    attendee = request.user.profile
    attendees = meetup.attendees
    attendees.remove(attendee)
    print(f'Cancelled attending: {meetup.attendees}')
    messages.success(request, 'You are no longer attending this meetup!')
    
    context = {'meetup': meetup}
    return render(request, 'meetups/meetup-details.html', context)
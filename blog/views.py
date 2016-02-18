from django.shortcuts import render, get_object_or_404, redirect
from .models import Show, Network, Day

def home(request):
    return render(request, 'blog/home.html')

def monday_list(request):
    day = Show.objects.filter(day__day="Monday")
    return render(request, 'blog/monday_list.html', {'show':show})















#def show_edit(request, pk):
#    show = get_object_or_404(Show, pk=pk)
#    if request.method == "POST":
#        form = ShowForm(request.POST, instance=show)
#        if form.is_valid():
#            show = form.save(commit=False)
#            show.save()
#            return redirect('show_detail', pk=show.pk)
#    else:
#        form = ShowForm(instance=show)
#    return render(request, 'blog/show_edit.html', {'form': form})

#def show_new(request):
#   if request.method == "POST":
#       form = ShowForm(request.POST)
#
#       if form.is_valid():
#           show = form.save(commit = False)
#           show.save()
#           return redirect('show_detail', pk=show.pk)
#   else:
#       form =ShowForm()
#   return render(request, 'blog/show_edit.html', {'form':form})
#
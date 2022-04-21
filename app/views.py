from django.shortcuts import render, HttpResponse,get_object_or_404
from .models import contact
from django.db.models import Q

from django.views.generic.edit import CreateView,UpdateView,DeleteView

#TO FETCH RESULT WITH MULTIPLE MODEL FIELDS, WE HAVE TO WORK WITH Q OBJECTS WHICH IS IMPORTED AS ABOVE

#GET OBJECT OR 404 TRIES TO GET AN OBJECT FROM PARTICULAR MODEL ANF IF NOT FOUND THEN IT DISPLAYS 404 ERROR
# Create your views here.

from django.shortcuts import redirect


def index(request):
    context= { 'contacts':contact.objects.all()
    }
    return render(request,'index.html', context)

    
def detail(request,id):
    context={
            # HERE WE WILL SEND THE CONTACT WHICH WILL CONTENT THE OBJECT WITH THE PARTICULAR ID
           # get_object_or_404(ARG,KWARG) TAKES TWO VALUE AS ARGUMENT WHICH ARE (NAME_OF_MODEL,PRIMARY KEY)
            'contact': get_object_or_404(contact,pk=id)

    }
    return render(request,'detail.html',context)

    
def search(request):
    if request.GET:
        search_term= request.GET['search_term']   #get('search_term') here search_term is the name given in the base.html 

        #search_results = contact.objects.filter(name__icontains=search_term) ## SEARCHING THOSE CONTENTS WHOSE NAME MATCHES WITH SEARCH_TERM AND DISPLAYING IT
        # search_results = contact.objects.filter(email__icontains=search_term)  ## SEARCHING THOSE CONTENTS WHOSE EMAIl MATCHES WITH SEARCH_TERM AND DISPLAYING IT
        

        #Q is used so that all the model fields(name,email,info,phoneno) can be used to get the searched term whereas above steps can only 
        # be used to get search results of one field type . ie. in first line name is used and in 2nd line email is used
        
        search_results = contact.objects.filter(
            Q(name__icontains=search_term) |
            Q(email__icontains=search_term) |
            Q(phone__iexact=search_term)   |
            Q(info__icontains=search_term) 
        )
        
        
        context={
            'search_term':search_term,
            'contacts':search_results,
        }
    else:
        return redirect('index') # this means if localhost/search is passed in url then in will redirect to the home page
    return render(request,'search.html',context)

#A view that displays a form for creating an object, redisplaying the form with validation errors (if there are any) and saving the object.




#createview,updateview and deleteview are the Form handling with class-based views 
class ContactCreateView(CreateView):
    model= contact
    template_name='create.html'
    fields=['name','email','phone','info','gender','image']
    success_url='/'


class ContactUpdateView(UpdateView):
    model= contact
    template_name='update.html'
    fields=['name','email','phone','info','gender','image']
    #success_url='/'          # IF WE KEEP THIS THEN AFTER UPDATING IT WILL RETURN TO THE HOME(INDEX) PAGE SO TO REMAIN IN THAT SAME DETAIL PAGE AFTER UPDATING, WE DO:
    

    #WE OVERRIDE THE SUCCESS URL WITH FORM_VALID, IT TAKES ARGUMENT SELF AND FORM
    def form_valid(self,form):
        instance=form.save()
        return redirect('detail',instance.pk)



class ContactDeleteView(DeleteView):
    model= contact
    template_name='delete.html'
    success_url='/'
    #FIELD IS NOT REQUIRED AS IT IS DELETED FROM THE DETAIL PAGE i.e AN INDIVIDUAL PAGE ITSELF


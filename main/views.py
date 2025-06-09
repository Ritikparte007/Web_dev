from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage, QuoteRequest
from .forms import ContactForm, QuoteForm

def home(request):
    """Homepage with hero section and service overview"""
    
    # Services data
    services = [
        {
            'title': 'Website Development',
            'description': 'Professional responsive websites with 7-day delivery',
            'price': '₹15,000 - ₹75,000',
            'delivery': '3-7 days',
            'features': ['Responsive Design', 'SEO Optimized', 'WhatsApp Integration', 'Admin Panel']
        },
        {
            'title': 'Game Development',
            'description': 'Custom games and interactive applications',
            'price': '₹25,000 - ₹1,50,000',
            'delivery': '7-14 days',
            'features': ['2D/3D Games', 'Mobile Games', 'Web Games', 'Unity/HTML5']
        },
        {
            'title': 'Mobile Apps',
            'description': 'iOS and Android applications',
            'price': '₹40,000 - ₹2,00,000',
            'delivery': '10-21 days',
            'features': ['Cross Platform', 'Native Performance', 'App Store Ready', 'Backend Integration']
        },
        {
            'title': 'Django Development',
            'description': 'Backend systems, APIs, and web applications',
            'price': '₹30,000 - ₹1,00,000',
            'delivery': '5-10 days',
            'features': ['REST APIs', 'Admin Panels', 'Database Design', 'Payment Integration']
        }
    ]
    
    # Stats for homepage
    stats = {
        'projects_completed': 150,
        'happy_clients': 120,
        'years_experience': 5,
        'avg_delivery_days': 7
    }
    
    # Why choose us points
    why_choose = [
        {
            'title': 'Fast Delivery',
            'description': 'Most projects delivered within 7 days',
            'icon': '⚡'
        },
        {
            'title': 'Quality Code',
            'description': 'Clean, maintainable, and scalable code',
            'icon': '💎'
        },
        {
            'title': 'Support',
            'description': '3 months free support after delivery',
            'icon': '🛠️'
        },
        {
            'title': 'Fair Pricing',
            'description': 'Transparent pricing, no hidden costs',
            'icon': '💰'
        }
    ]
    
    context = {
        'services': services,
        'stats': stats,
        'why_choose': why_choose,
        'page_title': 'Professional Web Development Services | 7-Day Delivery'
    }
    
    return render(request, 'main/home.html', context)

def about(request):
    """About page with developer info"""
    
    skills = [
        {'name': 'Python/Django', 'level': 95},
        {'name': 'JavaScript/React', 'level': 90},
        {'name': 'HTML/CSS/Bootstrap', 'level': 98},
        {'name': 'Mobile Development', 'level': 85},
        {'name': 'Game Development', 'level': 80},
        {'name': 'Database Design', 'level': 88}
    ]
    
    experience = [
        {
            'year': '2019-2020',
            'title': 'Freelance Developer',
            'description': 'Started freelancing, built 20+ websites'
        },
        {
            'year': '2020-2022',
            'title': 'Full Stack Developer',
            'description': 'Worked with multiple agencies, 50+ projects'
        },
        {
            'year': '2022-Present',
            'title': 'Senior Developer',
            'description': '100+ projects, team lead, mentor'
        }
    ]
    
    context = {
        'skills': skills,
        'experience': experience,
        'page_title': 'About - Professional Developer with 5+ Years Experience'
    }
    
    return render(request, 'main/about.html', context)

def contact(request):
    """Contact page with working form"""
    
    contact_info = {
        'phone': '+91 9876543210',
        'email': 'your@email.com',
        'whatsapp': '+91 9876543210',
        'address': 'Your City, India'
    }
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the message
            contact_message = form.save()
            
            # Show success message
            messages.success(
                request, 
                f'धन्यवाद {contact_message.name}! आपका message भेज दिया गया है। '
                f'24 घंटे में WhatsApp/Phone पर reply मिलेगा।'
            )
            
            # Optional: Send email notification to yourself
            try:
                send_mail(
                    subject=f'New Contact: {contact_message.subject}',
                    message=f'Name: {contact_message.name}\n'
                           f'Email: {contact_message.email}\n'
                           f'Phone: {contact_message.phone}\n'
                           f'Message: {contact_message.message}',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=['your@email.com'],  # Your email
                    fail_silently=True,
                )
            except:
                pass  # Email sending is optional
            
            # Redirect to avoid form resubmission
            return redirect('main:contact')
        else:
            messages.error(request, 'कुछ errors हैं form में। Please check और try again.')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
        'contact_info': contact_info,
        'page_title': 'Contact - Get Your Project Quote'
    }
    
    return render(request, 'main/contact.html', context)

def get_quote(request):
    """Quote request page (we'll add this later)"""
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote_request = form.save()
            messages.success(
                request, 
                f'Quote request भेजा गया {quote_request.name}! '
                f'24 घंटे में detailed quote WhatsApp पर भेजेंगे।'
            )
            return redirect('main:home')
    else:
        form = QuoteForm()
    
    return render(request, 'main/get_quote.html', {'form': form})
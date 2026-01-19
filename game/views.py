from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Card, UserScore
import random
import json
from django.views.decorators.csrf import csrf_exempt

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard_view(request):
    user_scores = UserScore.objects.filter(user=request.user).order_by('-score')[:5]
    best_score = UserScore.objects.filter(user=request.user).order_by('-score').first()
    leaderboard = UserScore.objects.order_by('-score')[:10]
    
    context = {
        'scores': user_scores,
        'best_score': best_score,
        'leaderboard': leaderboard,
        'username': request.user.username
    }
    return render(request, 'dashboard.html', context)

@login_required
def game_view(request):
    return render(request, 'game.html')

@login_required
def get_cards_api(request):
    all_cards = list(Card.objects.all())
    # Default to 8 pairs (16 cards) if we have enough, else use what we have
    num_pairs = 8
    
    if not all_cards:
        return JsonResponse({'cards': []})
        
    if len(all_cards) < num_pairs:
        # If we have few cards, just reuse them
        selected_cards = (all_cards * num_pairs)[:num_pairs]
    else:
        selected_cards = random.sample(all_cards, num_pairs)
    
    game_cards = []
    for card in selected_cards:
        card_data = {
            'id': card.id,
            'title': card.title,
            'image': card.image.url
        }
        game_cards.append(card_data) # Pair 1
        game_cards.append(card_data) # Pair 2
    
    random.shuffle(game_cards)
    # Add unique ID for frontend tracking to distinguish duplicates
    for idx, card in enumerate(game_cards):
        card['unique_id'] = idx
        
    return JsonResponse({'cards': game_cards})

@csrf_exempt
@login_required
def save_score_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            score = data.get('score', 0)
            time_taken = data.get('time_taken', 0)
            UserScore.objects.create(user=request.user, score=score, time_taken=time_taken)
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error'}, status=400)

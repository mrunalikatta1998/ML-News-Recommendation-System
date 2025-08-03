from django.http import JsonResponse
from newsrecapis.MLModels.NaiveBayse import train_nb_model
from newsrecapis.MLModels.LogisticRegression import train_lr_model
from newsrecapis.MLModels.SVM import train_svc_model
from newsrecapis.MLModels.NaiveBayse import train_nb_model
from newsrecapis.News.NewsClassProcessor import get_newsWithClass
import jwt
from django.http import JsonResponse
from django.conf import settings
from .models import User

def trainModel(request):
    try:
        # train_nb_model()  # Call the function to train the model
        # return JsonResponse({"message": "Model training successful"}, status=200)

        #train_lr_model()  # Call the function to train the model
        #return JsonResponse({"message": "Model training successful"}, status=200)

        train_svc_model()  # Call the function to train the model
        return JsonResponse({"message": "Model training successful"}, status=200)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

def getRecommendedNews(request):
    auth_header = request.headers.get('Authorization', None)
    if not auth_header or not auth_header.startswith('Bearer '):
        return JsonResponse({"error": "Authorization header missing or invalid"}, status=401)

    token = auth_header.split(' ')[1]

    try:
        # Decode the JWT token
        decoded_token = jwt.decode(
            token,
            settings.SECRET_KEY,  # Use the same secret key used to sign the token
            algorithms=["HS256"]  # Specify the signing algorithm
        )

        # Extract user information from the token payload
        user_id = decoded_token.get('user_id')  # This depends on your token structure
        
        user = User.objects.get(id=user_id)
        preferedCategories = user.preferred_news_categories.split(',')

        # Use `user_id` or `username` for your logic
        model_name = request.GET.get('model_name', None)
        recommended_news = get_newsWithClass(modelName=model_name)

        return JsonResponse({"recommended_news": recommended_news, "preferedCategories": preferedCategories}, status=200)

    except jwt.ExpiredSignatureError:
        return JsonResponse({"error": "Token has expired"}, status=401)
    except jwt.InvalidTokenError:
        return JsonResponse({"error": "Invalid token"}, status=401)

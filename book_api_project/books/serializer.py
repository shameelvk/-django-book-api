from rest_framework import serializers
from .models import Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


    def validate(self, data):
        
        required_fields = ['title', 'author', 'isbn', 'publication_date']
        for field in required_fields:
            if field not in data:
                raise serializers.ValidationError(f"{field} field is required")

       
        if not isinstance(data['title'], str):
            raise serializers.ValidationError("Title must be a string")
        if not isinstance(data['author'], str):
            raise serializers.ValidationError("Author must be a string")
        if not isinstance(data['isbn'], str):
            raise serializers.ValidationError("ISBN must be a string")
        if not isinstance(data['publication_date'], date):
            raise serializers.ValidationError("Publication date must be a valid date object")
        if len(data.get('isbn', '')) != 13:
            raise serializers.ValidationError("ISBN must be 13 characters long")
        
        

        return data
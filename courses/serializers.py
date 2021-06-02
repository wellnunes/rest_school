from rest_framework import serializers
from django.db.models import Avg

from .models import Course, Rating


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Rating
        fields = (
            'id',
            'course',
            'name',
            'email',
            'comment',
            'rating',
            'created_at',
            'status'
        )

    # validate_{field}
    def validate_rating(self, value):
        if value in range(1, 5):
            return value
        raise serializers.ValidationError('the rating needs to be at least 1 and at most 5')


class CourseSerializer(serializers.ModelSerializer):
    # nested relationship
    # ratings = RatingSerializer(many=True, read_only=True)

    # hyperlinked related field
    # ratings = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='rating-detail')

    # primary key related field
    ratings = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    rating_average = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = (
            'id',
            'title',
            'url',
            'created_at',
            'status',
            'ratings',
            'rating_average'
        )

    # value for method field(rating_average)  [ get_{field} ]
    def get_rating_average(self, obj):
        average = obj.ratings.aggregate(Avg('rating')).get('rating__avg')
        if average is None:
            return 0
        return round(average * 2) / 2

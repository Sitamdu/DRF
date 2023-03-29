from rest_framework import serializers
from home.models import Streaming,WatchList,Reviews


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reviews
        fields = "__all__"


class WatchlistSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = WatchList
        fields ="__all__"

class StreamSerializer(serializers.ModelSerializer):
    watchlist = WatchlistSerializer(many=True,read_only=True)

    class Meta:
        model = Streaming
        fields = "__all__"

        # fields = ['id','name','description']
        # exclude = ['active']

    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("name and description should be different!")
    #     else:
    #         return data
    #
    #
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short!")
    #     else:
    #         return value



# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short!")
#
#
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
#
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
#
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
#
#
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("name and description should be different!")
#         else:
#             return data


    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short!")
    #     else:
    #         return value


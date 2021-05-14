from flask import Blueprint, request, jsonify, jsoncd
from tv_inventory.helpers import token_required
from tv_inventory.models import User, Review, tv_schema, tv_schemas, db

api = Blueprint('api', __name__, url_prefix='/api')

#create review endpoint
@api.route('/reviews', methods = ['POST'])
@token_required
def create_review(current_user_token): #coming from token_required decorator
    show = request.json['show']
    season = request.json['season']
    episode= request.json['episode']
    rating = request.json['rating']
    user_token = current_user_token.token
   
    review = Review(show, season, episode, rating,user_token=user_token)
    db.session.add(review)
    db.session.commit()
    response = tv_schema.dump(review)
    return jsonify(response)

#retrieve all reviews
@api.route('/reviews', methods = ['GET'])
@token_required
def get_reviews(current_user_token):
    owner = current_user_token.token
    reviews = Review.query.filter_by(user_token = owner).all()
    response = tv_schemas.dump(reviews)
    return jsonify(response)

#retrieve one  endpoint
@api.route('/reviews/<id>', methods = ['GET'])
@token_required
def get_review(current_user_token, id):
    review = Review.query.get(id)
    response = tv_schema.dump(review)
    return jsonify(response)

#update review by id
@api.route('/reviews/<id>', methods = ['POST', 'PUT'])
@token_required
def update_review(current_user_token, id):
    review = Review.query.get(id)
    print(request.json)
    #different notation from instantiation
    review.show = request.json['show']
    review.season = request.json['season']
    review.episode = request.json['episode']
    review.rating = request.json['rating']
    review.user_token = current_user_token.token 
    print("rating", review.rating)

    # # #different notation from instantiation
    db.session.commit()
    response = tv_schema.dump(review)
    return jsonify(response)

#delete review by ID
@api.route('/reviews/<id>', methods = ['DELETE'])
@token_required
def delete_review(current_user_token,id):
    review=Review.query.get(id)
    db.session.delete(review)
    db.session.commit()
    response=tv_schema.dump(review)
    return jsonify(response)



    








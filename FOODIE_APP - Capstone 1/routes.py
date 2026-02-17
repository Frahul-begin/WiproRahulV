from flask import Blueprint, request, jsonify
from models import users, restaurants, dishes, orders, ratings

api = Blueprint("api", __name__)

# ---------------- USER ----------------
@api.route("/api/v1/users/register", methods=["POST"])
def register_user():
    data = request.get_json(force=True)

    if "name" not in data:
        return jsonify({"error": "Name is required"}), 400

    user = {
        "id": len(users) + 1,
        "name": data["name"]
    }
    users.append(user)
    return jsonify(user), 201

@api.route("/api/v1/users", methods=["GET"])
def get_all_users():
    if not users:
        return jsonify({"message": "No users found"}), 404

    return jsonify(users), 200

# ---------------- RESTAURANT ----------------
@api.route("/api/v1/restaurants", methods=["POST"])
def add_restaurant():
    data = request.get_json(force=True)

    if "name" not in data or "location" not in data:
        return jsonify({"error": "Invalid data"}), 400

    restaurant = {
        "id": len(restaurants) + 1,
        "name": data["name"],
        "location": data["location"]
    }
    restaurants.append(restaurant)
    return jsonify(restaurant), 201

@api.route("/api/v1/restaurants/<int:restaurant_id>", methods=["GET"])
def get_restaurant(restaurant_id):
    for restaurant in restaurants:
        if restaurant["id"] == restaurant_id:
            return jsonify(restaurant), 200
    return jsonify({"error": "Restaurant not found"}), 404



# ---------------- DISH ----------------
@api.route("/api/v1/dishes", methods=["POST"])
def add_dish():
    data = request.get_json(force=True)

    if "name" not in data or "price" not in data:
        return jsonify({"error": "Invalid data"}), 400

    dish = {
        "id": len(dishes) + 1,
        "name": data["name"],
        "price": data["price"]
    }
    dishes.append(dish)
    return jsonify(dish), 201

@api.route("/api/v1/dishes", methods=["GET"])
def get_all_dishes():
    if not dishes:
        return jsonify({"message": "No dishes available"}), 404

    return jsonify(dishes), 200


# ---------------- ORDER ----------------
@api.route("/api/v1/orders", methods=["POST"])
def place_order():
    data = request.get_json(force=True)

    if "user_id" not in data or "dish_id" not in data:
        return jsonify({"error": "Invalid data"}), 400

    order = {
        "id": len(orders) + 1,
        "user_id": data["user_id"],
        "dish_id": data["dish_id"]
    }
    orders.append(order)
    return jsonify(order), 201

@api.route("/api/v1/orders", methods=["GET"])
def get_all_orders():
    if not orders:
        return jsonify({"message": "No orders found"}), 404

    return jsonify(orders), 200

# ---------------- ADMIN ----------------
@api.route("/api/v1/admin/users", methods=["GET"])
def admin_get_users():
    return jsonify(users), 200

@api.route("/api/v1/admin/restaurants", methods=["GET"])
def admin_get_restaurants():
    return jsonify(restaurants), 200

@api.route("/api/v1/admin/dishes", methods=["GET"])
def admin_get_dishes():
    return jsonify(dishes), 200

@api.route("/api/v1/admin/orders", methods=["GET"])
def admin_get_orders():
    return jsonify(orders), 200


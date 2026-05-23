# Storefront

A RESTful e-commerce API built with **Django 6.0** and **Django REST Framework**, featuring products, collections, cart management, ordering, customer profiles, reviews, product images, tagging, and likes — all secured with JWT authentication.

---

## Tech Stack

| Layer      | Technology                            |
| ---------- | ------------------------------------- |
| Framework  | Django 6.0, Django REST Framework 3.x |
| Database   | PostgreSQL (SQLite3 fallback)         |
| Auth       | JWT (djoser + SimpleJWT)              |
| Filtering  | django-filter, DRF search/ordering    |
| Routing    | DRF nested routers                    |
| Images     | Pillow                                |
| Signal Bus | Custom `order_created` Django signal  |
| Dev Tools  | django-debug-toolbar, django-stubs    |

---

## Project Structure

```
storefront/
├── .env                          # Environment variables (DB creds)
├── .env.example
├── Pipfile                       # Python dependencies
├── manage.py
├── db.sqlite3
│
├── storefront/                   # Django project configuration
│   ├── settings.py               # DRF, djoser, simplejwt, debug toolbar config
│   ├── urls.py                   # Root URL conf
│   ├── asgi.py / wsgi.py
│
├── core/                         # Custom user model + cross-app logic
│   ├── models.py                 # User (extends AbstractUser, unique email)
│   ├── serializers.py            # UserCreateSerializer, UserSerializer
│   ├── signals/handlers.py       # Listens to order_created signal
│
├── store/                        # Main e-commerce app
│   ├── models.py                 # Product, Collection, Cart, CartItem, Order,
│   │                             # OrderItem, Customer, Review, ProductImage,
│   │                             # Promotion, Address
│   ├── serializers.py            # All CRUD + nested + order creation serializers
│   ├── views.py                  # ProductViewSet, CartViewSet, OrderViewSet, etc.
│   ├── urls.py                   # Routed endpoints for store API
│   ├── filters.py                # ProductFilter (collection_id, unit_price range)
│   ├── pagination.py             # DefaultPagination (10 per page)
│   ├── permissions.py            # IsAdminOrReadOnly, ViewCustomerHistoryPermission
│   ├── admin.py                  # Custom admin configs with inlines & actions
│   ├── signals/
│   │   ├── __init__.py           # order_created Signal definition
│   │   └── handlers.py           # Auto-create Customer on User post_save
│   └── management/commands/
│       ├── seed_db.py            # Management command to seed DB
│       └── seed.sql              # Seed data (200+ products, 10 collections)
│
├── likes/                        # Generic foreign key likes
│   └── models.py                 # LikedItem (user + GFK to any model)
│
├── tags/                         # Generic tagging system
│   ├── models.py                 # Tag, TaggedItem (with custom manager)
│   ├── admin.py                  # TagAdmin with search
│   └── views.py
│
├── playground/                   # Test views
│   ├── urls.py                   # hello/ endpoint
│   └── views.py                  # say_hello - creates order in transaction
│
├── media/store/images/           # Uploaded product images
└── seed/                         # Additional SQL seed files
    ├── seed.sql
    └── store_customer.sql
```

---

## Features

### Products & Collections

- Full CRUD for products and collections
- Product search (`title`, `description`) and ordering (`unit_price`, `last_update`)
- Filter by `collection_id` and `unit_price` range
- Paginated listings (10 per page)
- Automatic slug generation
- Product images (upload multiple per product)

### Cart

- UUID-based cart identification (no login required)
- Upsert behavior: adding an existing product increments quantity
- Nested cart items with computed `total_price`

### Orders

- Create orders from cart contents (clears cart on completion)
- Payment status tracking (`Pending`, `Completed`, `Failed`)
- Staff can update payment status; users see only their own orders
- Custom `order_created` signal on order placement

### Customers

- Auto-created via signal when a user registers
- `me` endpoint for profile retrieval/update
- `history` endpoint (requires `view_history` permission)
- Membership levels: Bronze, Silver, Gold

### Reviews

- Product-scoped nested reviews (`/products/{pk}/reviews/`)

### Authentication

- JWT tokens (`auth/jwt/create`, `refresh`, `verify`)
- Djoser user management (register, activate, reset password, set password)

### Admin Interface

- Custom Product admin with inventory filter, bulk clear action, image previews
- Customer admin with order count and filtered drill-down
- Order admin with inline order items

---

## API Endpoints

### Auth (`/auth/`)

| Method        | Endpoint                              | Description             |
| ------------- | ------------------------------------- | ----------------------- |
| POST          | `/auth/users/`                        | Register new user       |
| GET           | `/auth/users/`                        | List users (admin)      |
| GET/PUT/PATCH | `/auth/users/me/`                     | Current user profile    |
| POST          | `/auth/users/activation/`             | Activate account        |
| POST          | `/auth/users/resend_activation/`      | Resend activation email |
| POST          | `/auth/users/reset_password/`         | Request password reset  |
| POST          | `/auth/users/reset_password_confirm/` | Confirm password reset  |
| POST          | `/auth/users/set_password/`           | Set new password        |
| POST          | `/auth/users/set_username/`           | Change username         |
| POST          | `/auth/jwt/create/`                   | Obtain JWT pair         |
| POST          | `/auth/jwt/refresh/`                  | Refresh access token    |
| POST          | `/auth/jwt/verify/`                   | Verify token validity   |

### Store (`/store/`)

| Method               | Endpoint                                | Description                    |
| -------------------- | --------------------------------------- | ------------------------------ |
| GET/POST             | `/store/products/`                      | List / Create product          |
| GET/PUT/PATCH/DELETE | `/store/products/{id}/`                 | Product detail                 |
| GET/POST             | `/store/products/{id}/reviews/`         | List / Create review           |
| GET/PUT/PATCH/DELETE | `/store/products/{id}/reviews/{r_id}/`  | Review detail                  |
| GET/POST             | `/store/products/{id}/images/`          | List / Add product image       |
| GET/DELETE           | `/store/products/{id}/images/{img_id}/` | Image detail                   |
| GET/POST             | `/store/collections/`                   | List / Create collection       |
| GET/PUT/PATCH/DELETE | `/store/collections/{id}/`              | Collection detail              |
| POST                 | `/store/carts/`                         | Create cart                    |
| GET/DELETE           | `/store/carts/{uuid}/`                  | Retrieve / Delete cart         |
| GET/POST             | `/store/carts/{uuid}/items/`            | List / Add cart item           |
| GET/PATCH/DELETE     | `/store/carts/{uuid}/items/{item_id}/`  | Cart item detail               |
| GET/POST             | `/store/customers/`                     | List / Create customer (admin) |
| GET/PUT/PATCH/DELETE | `/store/customers/{id}/`                | Customer detail                |
| GET/PUT              | `/store/customers/me/`                  | Current customer profile       |
| GET                  | `/store/customers/{id}/history/`        | Customer order history         |
| GET/POST             | `/store/orders/`                        | List / Place order             |
| GET/PATCH/DELETE     | `/store/orders/{id}/`                   | Order detail                   |

---

## Models

| Model                | Key Fields                                                                   | Notes                           |
| -------------------- | ---------------------------------------------------------------------------- | ------------------------------- |
| `User`               | `email` (unique), `username`, `password`                                     | Extends `AbstractUser`          |
| `Customer`           | `user` (OneToOne), `phone`, `birth_date`, `membership`                       | Auto-created on user signup     |
| `Product`            | `title`, `slug`, `description`, `unit_price`, `inventory`, `collection` (FK) | Supports multiple images        |
| `Collection`         | `title`, `featured_product` (nullable FK)                                    |                                 |
| `Cart`               | `id` (UUID), `created_at`                                                    |                                 |
| `CartItem`           | `cart` (FK), `product` (FK), `quantity`                                      | Unique together: cart + product |
| `Order`              | `customer` (FK), `placed_at`, `payment_status`                               | Pending / Complete / Failed     |
| `OrderItem`          | `order` (FK), `product` (FK), `quantity`, `unit_price`                       |                                 |
| `Review`             | `product` (FK), `name`, `description`                                        |                                 |
| `ProductImage`       | `product` (FK), `image` (ImageField)                                         | Uploads to `store/images`       |
| `Promotion`          | `description`, `discount`                                                    | M2M with Product                |
| `Address`            | `customer` (FK), `street`, `city`, `zip`                                     |                                 |
| `Tag` / `TaggedItem` | Label + GFK                                                                  | Generic tagging system          |
| `LikedItem`          | `user` (FK) + GFK                                                            | Generic likes                   |

---

## Setup

### Prerequisites

- Python 3.14+
- PostgreSQL (or SQLite — no config needed)

### Installation

```bash
# 1. Clone and enter the project
cd storefront

# 2. Create virtual environment inside project
export PIPENV_VENV_IN_PROJECT=1

# 3. Install dependencies
pipenv install

# 4. Activate virtual environment
pipenv shell

# 5. Configure database (optional — defaults to SQLite)
#    Copy .env.example to .env and fill in PostgreSQL credentials:
cp .env.example .env
```

### Run

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py seed_db      # Seed 200+ products and collections
python manage.py runserver
```

### Seed Data

The included `seed_db` management command populates the database with:

- **10 collections** (Flowers, Grocery, Beauty, Cleaning, etc.)
- **200+ products** with realistic titles, prices, and inventory counts
- Additional SQL files in `seed/` directory for customers

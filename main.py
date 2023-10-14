from app.models.user import User
from app.database.persistence import get_all, get_for_id, update, delete, create


# Get all
print(" \n".join(map(str, get_all("user"))))

# Get for id
print(get_for_id(1, "user"))

# Update
u1 = User(id=1, nome="Hállan", idade=12)
update(u1)

# Delete
delete(1, "user")

# Create
u1 = User(nome="Hállan", idade=12)
create(u1)

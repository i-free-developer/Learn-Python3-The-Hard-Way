# TravelApp by Rails

1. We created two models named Tag and Destinations.
2. In the model files, we used the methods `has_many` and `belongs_to` define an association between Tag and Destination:
   - `has_many :destinations` denotes that a single Tag can have multiple Destinations.
   - `belongs_to :tag` denotes that each Destination belongs to a single Tag.

The `has_many` / `belongs_to` pair is frequently used to define one-to-many relationships. A few examples are:

- a Library has many Books; a Book belongs to a Library
- an Album has many Photos; a Photo belongs to an Album
- a Store has many Products; a Product belongs to a Store

rails new TravelApp
bundle install
rails generate model Tag # Generate a model named Tag
rails generate model Destination

In app/models/tag.rb add a has_many method, like this:

class Tag < ActiveRecord::Base
  has_many :destinations
end

In app/models/destination.rb, add a belongs_to method:

belongs_to :tag

Open the migration file in db/migrate/ for the tags table, and add the following columns:

a string column called title

a string column called image

```ruby
class CreateTags < ActiveRecord::Migration
  def change
      create_table :tags do |t|
      t.string :title
      t.string :image
      t.timestamps
		end
	end
end
```


in the migration file for the destinations table, add the following columns:

- a `string` column called `name`
- a `string` column called `image`
- a `string` column called `description`
- the line `t.references :tag`

```ruby
class CreateDestinations < ActiveRecord::Migration
  def change
		create_table :destinations do |t|
		t.string :name
		t.string :image
		t.string :description
		t.references :tag
  		t.timestamps
		end
	end
end
```
class CreateLuminosities < ActiveRecord::Migration[5.1]
  def change
    create_table :luminosities do |t|
      t.integer :value
      t.timestamps
    end
  end
end

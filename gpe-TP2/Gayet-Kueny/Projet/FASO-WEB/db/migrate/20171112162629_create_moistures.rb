class CreateMoistures < ActiveRecord::Migration[5.1]
  def change
    create_table :moistures do |t|
      t.integer :value
      t.timestamps
    end
  end
end

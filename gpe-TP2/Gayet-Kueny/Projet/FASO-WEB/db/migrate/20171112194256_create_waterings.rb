class CreateWaterings < ActiveRecord::Migration[5.1]
  def change
    create_table :waterings do |t|
      t.boolean :state
      t.timestamps
    end
  end
end

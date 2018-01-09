class CreateSettings < ActiveRecord::Migration[5.1]
  def change
    create_table :settings do |t|
      t.string :wifi_name, default: ''
      t.string :wifi_password, default: ''
      t.integer :moisture_treshold, default: 0
      t.integer :temperature_treshold, default: 0
      t.integer :humidity_treshold, default: 0
      t.timestamps
    end
  end
end

class AddTempTreshMinMax < ActiveRecord::Migration[5.1]
  def change
    add_column :settings, :temperature_treshold_min, :integer, default: 0
    add_column :settings, :temperature_treshold_max, :integer, default: 0
  end
end

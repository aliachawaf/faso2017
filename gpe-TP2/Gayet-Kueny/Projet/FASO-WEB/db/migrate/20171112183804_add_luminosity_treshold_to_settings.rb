class AddLuminosityTresholdToSettings < ActiveRecord::Migration[5.1]
  def change
    add_column :settings, :luminosity_treshold, :integer, default: 0
  end
end

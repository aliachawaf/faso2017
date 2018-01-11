class SettingsController < ApplicationController

  def show
    @setting = Setting.first
  end

  def update
    Setting.first.update(setting_params)
  end

  private

  def setting_params
    params.require(:setting).permit(:wifi_name, :wifi_password, :moisture_treshold, :temperature_treshold_min, :temperature_treshold_max)
  end
end

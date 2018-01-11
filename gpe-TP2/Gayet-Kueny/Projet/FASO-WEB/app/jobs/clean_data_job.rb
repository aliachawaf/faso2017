class CleanDataJob < ApplicationJob
  queue_as :default

  def perform(*args)
    # Do something later
    Temperature.where('created_at < ?', Time.now - 1.week).destroy_all
    Humidity.where('created_at < ?', Time.now - 1.week).destroy_all
    Luminosity.where('created_at < ?', Time.now - 1.week).destroy_all
    Moisture.where('created_at < ?', Time.now - 1.week).destroy_all
    Watering.where('created_at < ?', Time.now - 1.week).destroy_all
  end
end

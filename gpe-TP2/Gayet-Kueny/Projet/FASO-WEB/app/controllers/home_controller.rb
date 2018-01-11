class HomeController < ApplicationController
    before_action :redirect

    def index

    end

    private

    def redirect
        CleanDataJob.perform_later
        redirect_to dashboard_path
    end
end

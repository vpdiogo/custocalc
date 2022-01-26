from flask import Blueprint, flash, redirect, render_template, request

from .controller import (
    calculate_plan_30,
    calculate_plan_60,
    calculate_plan_120,
    calculate_without_plan,
)

site = Blueprint("site", __name__)


@site.route("/", methods=["GET", "POST"])
def index():
    plan_value = []
    data_input = []
    if request.method == "POST":
        origin = request.form.get("origin")
        destination = request.form.get("destiny")
        time = request.form.get("time")
        plan = request.form.get("plan")

        if not origin or not destination or not time or not plan:
            flash("Verifique o preenchimento dos campos", "danger")
            return redirect(request.url)

        try:
            int(time)
        except ValueError:
            flash("O tempo deve ser informado em minutos", "danger")
            return redirect(request.url)

        plan_value.append(
            calculate_without_plan(int(origin), int(destination), int(time))
        )

        if plan == "Plano 30":
            plan_value.append(
                calculate_plan_30(int(origin), int(destination), int(time))
            )
        if plan == "Plano 60":
            plan_value.append(
                calculate_plan_60(int(origin), int(destination), int(time))
            )
        if plan == "Plano 120":
            plan_value.append(
                calculate_plan_120(int(origin), int(destination), int(time))
            )

        data_input = [origin, destination, time, plan]

    return render_template("index.html", data=plan_value, data_input=data_input)

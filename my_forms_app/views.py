import datetime,math
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Count, Avg, Min, Max, StdDev, Sum
# from .forms import AbcForm, AbcModelForm
# from .models import AbcModel
from .forms import StudentForm, EducationProgramForm, ManagementMemberForm, FellowStudentForm
from .models import Student, EducationProgram, ManagementMember, FellowStudent




# -----------------------------------------------------



def add_student(request):
    # проверяю, что пользователь отправил данные
    if request.method == 'POST':
        # передаю данные из формы
        form = StudentForm(request.POST, request.FILES)
        # Django проверяет, всё ли заполнено правильно
        if form.is_valid():
            # сохраняю данные в базу
            form.save()
            return redirect('my_app:students_result')  # перенаправление после успешной отправки
    else:
        form = StudentForm()
    # показываем HTML-шаблон с формой
    return render(request, 'add_student.html', {'form': form})

def students_result(request):
    sort_param = request.GET.get('sort')
    second_name_filter = request.GET.get('second_name', '')
    name_filter = request.GET.get('name', '')
    parent_name_filter = request.GET.get('parent_name', '')
    program_name_filter = request.GET.get('program_name', '')

    # сначала фильтрую
    students = Student.objects.all()
    if second_name_filter:
        students = students.filter(second_name__icontains=second_name_filter)
    if name_filter:
        students = students.filter(name__icontains=name_filter)
    if parent_name_filter:
        students = students.filter(parent_name__icontains=parent_name_filter)
    if parent_name_filter:
        students = students.filter(parent_name__icontains=parent_name_filter)
    if program_name_filter:
        students = students.filter(program_name__icontains=program_name_filter)

    # потом сортирую
    if sort_param:
        students = students.order_by(sort_param)

    program_stats = students.values('program_name').annotate(count=Count('id')).order_by('-count')

    return render(request, 'students_result.html', {
        'students': students,
        'current_sort': sort_param,
        'second_name_filter': second_name_filter,
        'name_filter': name_filter,
        'parent_name_filter': parent_name_filter,
        'program_name_filter': program_name_filter,
        'program_stats': program_stats
    })



# -----------------------------------------------------




def add_program(request):
    # проверяю, что пользователь отправил данные
    if request.method == 'POST':
        # передаю данные из формы
        form = EducationProgramForm(request.POST, request.FILES)
        # Django проверяет, всё ли заполнено правильно
        if form.is_valid():
            # сохраняю данные в базу
            form.save()
            return redirect('my_app:program_result')  # перенаправление после успешной отправки
    else:
        form = EducationProgramForm()
    # показываем HTML-шаблон с формой
    return render(request, 'add_program.html', {'form': form})

def program_result(request):
    sort_param = request.GET.get('sort')
    name_filter = request.GET.get('name', '')

    result = EducationProgram.objects.all()
    if name_filter:
        result = result.filter(name__icontains=name_filter)

    if sort_param:
        result = EducationProgram.objects.all().order_by(sort_param)

    most_popular = EducationProgram.objects.values('name').annotate(count=Count('id')).order_by('-count').first()

    return render(request, 'program_result.html', {
        'result': result,
        'current_sort': sort_param,
        'name_filter': name_filter,
        'most_popular': most_popular
    })



# -----------------------------------------------------


def add_managers(request):
    # проверяю, что пользователь отправил данные
    if request.method == 'POST':
        # передаю данные из формы
        form = ManagementMemberForm(request.POST, request.FILES)
        # Django проверяет, всё ли заполнено правильно
        if form.is_valid():
            # сохраняю данные в базу
            form.save()
            return redirect('my_app:managers_result')  # перенаправление после успешной отправки
    else:
        form = ManagementMemberForm()
    # показываем HTML-шаблон с формой
    return render(request, 'add_managers.html', {'form': form})

def managers_result(request):
    sort_param = request.GET.get('sort')
    second_name_filter = request.GET.get('second_name', '')
    name_filter = request.GET.get('name', '')
    parent_name_filter = request.GET.get('parent_name', '')
    role_filter = request.GET.get('role', '')
    program_name_filter = request.GET.get('program_name', '')

    # сначала фильтрую
    info = ManagementMember.objects.all()
    if second_name_filter:
        info = info.filter(second_name__icontains=second_name_filter)
    if name_filter:
        info = info.filter(name__icontains=name_filter)
    if parent_name_filter:
        info = info.filter(parent_name__icontains=parent_name_filter)
    if role_filter:
        info = info.filter(role__icontains=role_filter)
    if program_name_filter:
        info = info.filter(program_name__icontains=program_name_filter)

    # потом сортирую
    if sort_param:
        info = info.order_by(sort_param)

    role_stats = info.values('role').annotate(count=Count('id'))

    return render(request, 'managers_result.html', {
        'info': info,
        'current_sort': sort_param,
        'second_name_filter': second_name_filter,
        'name_filter': name_filter,
        'parent_name_filter': parent_name_filter,
        'role_filter': role_filter,
        'program_name_filter': program_name_filter,
        'role_stats': role_stats
    })



# -----------------------------------------------------


def add_fellows(request):
    # проверяю, что пользователь отправил данные
    if request.method == 'POST':
        # передаю данные из формы
        form = FellowStudentForm(request.POST, request.FILES)
        # Django проверяет, всё ли заполнено правильно
        if form.is_valid():
            # сохраняю данные в базу
            form.save()
            return redirect('my_app:fellows_result')  # перенаправление после успешной отправки
    else:
        form = FellowStudentForm()
    # показываем HTML-шаблон с формой
    return render(request, 'add_fellows.html', {'form': form})

def fellows_result(request):
    sort_param = request.GET.get('sort')
    second_name_filter = request.GET.get('second_name', '')
    name_filter = request.GET.get('name', '')
    parent_name_filter = request.GET.get('parent_name', '')
    program_name_filter = request.GET.get('program_name', '')

    # сначала фильтрую
    details = FellowStudent.objects.all()
    if second_name_filter:
        details = details.filter(second_name__icontains=second_name_filter)
    if name_filter:
        details = details.filter(name__icontains=name_filter)
    if parent_name_filter:
        details = details.filter(parent_name__icontains=parent_name_filter)
    if program_name_filter:
        details = details.filter(program_name__icontains=program_name_filter)

    # потом сортирую
    if sort_param:
        details = details.order_by(sort_param)

    program_stats = details.values('program_name').annotate(count=Count('id')).order_by('-count')

    return render(request, 'fellows_result.html', {
        'details': details,
        'current_sort': sort_param,
        'second_name_filter': second_name_filter,
        'name_filter': name_filter,
        'parent_name_filter': parent_name_filter,
        'program_name_filter': program_name_filter,
        'program_stats': program_stats
    })


# -----------------------------------------------------


def index(request):
    return render(request, "index.html")


# def datetime_nov(request):
#     datetime_now = datetime.datetime.now()
#     print(datetime_now)
#     context = {"key": datetime_now}
#     return render(request, "datetime_now.html", context)


# def var_list_dict(request):
#     var_main = 2
#     print(var_main)
#     list_main = [1, 2, 3, 4, 5]
#     print(list_main)
#     dict_main = {"x": 1, "y": 2}
#     print(dict_main)
#     context = {"var_main": var_main, "list_main": list_main, "dict_main": dict_main}
#     return render(request, "list_dict.html", context)





# def abc_form(request):
#     abc_form = AbcForm()
#     print(abc_form)
#     return render(request, "abc_form.html", {"abc_form": abc_form})


# def abc_get(request):
#     print(request.GET)
#     task_value = (request.GET.get("task"))
#     a_value = int(request.GET.get("a"))
#     b_value =int(request.GET.get("b")) 
#     c_value = int(request.GET.get("c")) 
#     print (a_value, b_value, c_value)
#     new_obj = AbcModel(task=task_value, a=a_value, b=b_value, c = c_value)
#     new_obj.save()
#     return redirect("orm_abc_app:abc_result")



# def abc_model_form(request):
#     print("request.method: ", request.method)
#     if request.method == "POST":
#         form = AbcModelForm(request.POST)
#         if form.is_valid():
#             print("\nform_is_valid:\n", form)
#             form.save()
#             return redirect("orm_abc_app:abc_result")
#     else:
#         form = AbcModelForm()
#         print("\nform_else:\n", form)
#     context = {"form": form}
#     print("\ncontext:\n", context)
#     return render(request, "abc_model_form.html", context)


# def abc_tweaks_form(request):
#     print("request.method: ", request.method)
#     if request.method == "POST":
#         form = AbcModelForm(request.POST)
#         if form.is_valid():
#             print("\nform_is_valid:\n", form)
#             form.save()
#             return redirect("orm_abc_app:abc_result")
#     else:
#         form = AbcModelForm()
#         print("\nform_else:\n", form)
#     context = {"form": form}
#     print("\ncontext:\n", context)
#     return render(request, "abc_tweaks_form.html", context)


# def solution(a, b, c):
#     if a + b == c:
#         result = " С равна сумме A и B"
#     else:
#         result = "С не равна сумме A и B"
#     return result


# def abc_result(request):
#     object_list = AbcModel.objects.all().order_by("-id")
#     print("\n\nobject_list: ", object_list)

#     last_object = object_list.values("task", "a", "b", "c")[0]
#     print("\n\nlast_object: ", last_object)
#     task_formulation = object_list.values("task")[0]
#     task_id = object_list.values("id")[0]["id"]
#     print("task_id task_formulation: ", task_id, task_formulation)


#     result = solution(last_object["a"], last_object["b"], last_object["c"])
#     print("\nresult: ", result)
  
    
    
#     update_obj = AbcModel.objects.filter(id=task_id)
#     update_result = result
#     update_obj.update(result = update_result )

#     # list
#     values_list = object_list.values_list()[0]
#     print("\nvalues_list: ", values_list)
#     task_formulation = values_list[1]
#     print("\ntask_formulation: ", task_formulation)
#     last_values = [values_list[1], values_list[2], values_list[3], values_list[4]]
#     print("\nlast_values:", last_values)


#     context = {
#         "last_object": last_object,
#         "task_formulation": task_formulation,
#         "last_values": last_values,
#         "result": result,
#     }
#     return render(request, "abc_result.html", context)


# def table(request):
#     # all = AbcModel.objects.all()
#     # all.delete()
#     # objects_list
#     objects_values = AbcModel.objects.values()
#     print("\nobjects_values:", objects_values)
#     # values_list
#     objects_values_list = (
#         AbcModel.objects.values_list().filter(id__gte=2).order_by("-id")
#     )  # [0:3]
#     print("\nobjects_values_list:", objects_values_list)
#     cur_objects = objects_values_list
#     statics_val = [
#         cur_objects.aggregate(Count("b")),
#         cur_objects.aggregate(Avg("b")),
#         cur_objects.aggregate(Min("b")),
#         cur_objects.aggregate(Max("b")),
#         cur_objects.aggregate(StdDev("b")),
#         cur_objects.aggregate(Sum("b")),
#     ]
#     print("\nstatics_val:", statics_val)
#     statics = {"statics_val": statics_val}
#     # fields_name
#     fields = AbcModel._meta.get_fields()
#     print("\nfields", fields)
#     verbose_name_list = []
#     name_list = []
#     for e in fields:
#         verbose_name_list.append(e.verbose_name)
#         name_list.append(e.name)
#     print("\nverbose_name_list:", verbose_name_list)
#     print("\nname_list", name_list)
#     field_names = verbose_name_list
#     context = {
#         "objects_values": objects_values,
#         "name_list": name_list,
#         "objects_values_list": objects_values_list,
#         "verbose_name_list": verbose_name_list,
#         "statics": statics,
#         "field_names": field_names,
#     }
#     return render(request, "table.html", context)

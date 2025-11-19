from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from stdmanage_app.models import Course, Session_Year, CustomUser, Student, Staff, Subject, Staff_Notifications, \
    Staff_leave, Staff_feedback, Student_feedback, Student_Notifications, Student_leave, Attendance_Report, Attendance, \
    StudentResult


@login_required(login_url='/')
def HOME(request):
    
    return render(request, "Student/home.html")


@login_required(login_url='/')
def STUDENT_NOTIFICATION(request):
    student = Student.objects.filter(admin=request.user.id)
    for i in student:
        student_id = i.id
        notification = Student_Notifications.objects.filter(student_id=student_id)
        context = {
            'notification': notification,
        }
        return render(request, "Student/notification.html", context)


@login_required(login_url='/')
def STUDENT_NOTIFICATION_MARK_AS_DONE(request, status):
    notification = Student_Notifications.objects.get(id=status)
    notification.status = 1
    notification.save()
    return redirect("student_notification")


def STUDENT_FEEDBACK(request):
    student_id = Student.objects.get(admin=request.user.id)
    feedback_history = Student_feedback.objects.filter(student_id=student_id)
    context = {
        'feedback_history': feedback_history
    }
    return render(request, "Student/feedback.html", context)


def STUDENT_FEEDBACK_SAVE(request):
    if request.method == "POST":
        feedback = request.POST.get('feedback')
        student = Student.objects.get(admin=request.user.id)
        feedback = Student_feedback(
            student_id=student,
            feedback=feedback,
            feedback_replay="",
        )
        feedback.save()
        messages.success(request, "Feedback has been send to Hod")
        return redirect('student_feedback')


def STUDENT_APPLY_LEAVE(request):
    student = Student.objects.filter(admin=request.user.id)
    for i in student:
        student_id = i.id

        student_leave_history = Student_leave.objects.filter(student_id=student_id)
        context = {
            'student_leave_history': student_leave_history
        }
        return render(request, 'Student/apply_leave.html', context)


def STUDENT_APPLY_LEAVE_SAVE(request):
    if request.method == 'POST':
        leave_date = request.POST.get('leave_date')
        leave_reason = request.POST.get('leave_reason')
        student = Student.objects.get(admin=request.user.id)
        leave = Student_leave(
            student_id=student,
            date=leave_date,
            message=leave_reason,
        )
        leave.save()
        messages.success(request, "Leave request has been successfully send")
        return redirect('student_apply_leave')


def STUDENT_VIEW_ATTENDANCE(request):
    student = Student.objects.get(admin=request.user.id)
    subject = Subject.objects.filter(course_id=student.course_id)
    action = request.GET.get('action')
    get_subject = None
    attendance_report = None

    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')
            get_subject = Subject.objects.get(id=subject_id)
            attendance_report = Attendance_Report.objects.filter(student_id=student,
                                                                 attendance_id__subject_id=subject_id)

    context = {
        'subject': subject,
        'action': action,
        'get_subject': get_subject,
        'attendance_report': attendance_report
    }

    return render(request, "Student/view_attendance.html", context)


def VIEW_RESULT(request):
    mark = None
    student = Student.objects.get(admin=request.user.id)
    result = StudentResult.objects.filter(student_id=student)

    for i in result:
        assignment_mark = i.assignment_mark
        exam_mark = i.exam_mark
        mark = assignment_mark + exam_mark

    context = {
        'result': result,
        'mark': mark,
    }
    return render(request, "Student/view_result.html", context)

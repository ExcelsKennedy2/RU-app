from django.core.management.base import BaseCommand
from academics.models import Program, Semester, Course

class Command(BaseCommand):
    help = "Populates Year 3 and 4 courses for all programs"

    def handle(self, *args, **kwargs):
        courses_data = [
            # Informatics
            ("Informatics", "INF 301", "Database Management Systems", 3, "1"),
            ("Informatics", "INF 302", "Systems Analysis and Design", 3, "2"),
            ("Informatics", "INF 401", "Machine Learning Fundamentals", 4, "1"),
            ("Informatics", "INF 402", "IT Project Management", 4, "2"),

            # Health Systems Management
            ("Health Systems Management", "HSM 301", "Health Services Management", 3, "1"),
            ("Health Systems Management", "HSM 302", "Epidemiology", 3, "2"),
            ("Health Systems Management", "HSM 401", "Strategic Health Planning", 4, "1"),
            ("Health Systems Management", "HSM 402", "Global Health Systems", 4, "2"),

            # Health Records & Information Management
            ("Health Records & Information Management", "HRIM 301", "Advanced Health Informatics", 3, "1"),
            ("Health Records & Information Management", "HRIM 302", "Records Digitization", 3, "2"),
            ("Health Records & Information Management", "HRIM 401", "Clinical Data Management", 4, "1"),
            ("Health Records & Information Management", "HRIM 402", "Data Governance in Healthcare", 4, "2"),

            # Information Sciences
            ("Information Sciences", "IS 301", "Knowledge Management", 3, "1"),
            ("Information Sciences", "IS 302", "Digital Libraries", 3, "2"),
            ("Information Sciences", "IS 401", "Advanced Information Retrieval", 4, "1"),
            ("Information Sciences", "IS 402", "Research in Information Science", 4, "2"),

            # Communication and Media Studies (Public Relations)
            ("Communication and Media Studies (Public Relations)", "CMSP 301", "Crisis Communication", 3, "1"),
            ("Communication and Media Studies (Public Relations)", "CMSP 302", "Public Relations Campaigns", 3, "2"),
            ("Communication and Media Studies (Public Relations)", "CMSP 401", "Media Ethics and Law", 4, "1"),
            ("Communication and Media Studies (Public Relations)", "CMSP 402", "Strategic PR Management", 4, "2"),

            # Communication and Media Studies (Journalism)
            ("Communication and Media Studies (Journalism)", "CMSJ 301", "Feature Writing", 3, "1"),
            ("Communication and Media Studies (Journalism)", "CMSJ 302", "Broadcast Journalism", 3, "2"),
            ("Communication and Media Studies (Journalism)", "CMSJ 401", "Investigative Journalism", 4, "1"),
            ("Communication and Media Studies (Journalism)", "CMSJ 402", "Media Research and Analysis", 4, "2"),
        ]

        created_count = 0

        for program_name, code, title, year, sem_code in courses_data:
            try:
                program = Program.objects.get(name=program_name)
                semester = Semester.objects.get(name=sem_code)
                course, created = Course.objects.get_or_create(
                    code=code,
                    defaults={
                        'title': title,
                        'program': program,
                        'year_of_study': year,
                        'semester': semester
                    }
                )
                if created:
                    created_count += 1
                    self.stdout.write(self.style.SUCCESS(f"Created: {code} - {title}"))
                else:
                    self.stdout.write(self.style.WARNING(f"Skipped (exists): {code}"))
            except Program.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"Program not found: {program_name}"))
            except Semester.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"Semester not found: {sem_code}"))

        self.stdout.write(self.style.SUCCESS(f"\n✅ Done! {created_count} courses added."))

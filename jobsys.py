jobs = []          
resume = {}        

while True:
    print("\n===== JOB PORTAL MENU =====")
    print("1. Add Job (Admin)")
    print("2. Upload Resume (User)")
    print("3. Match Jobs with Resume")
    print("4. View All Jobs")
    print("5. Exit")

    choice = input("Enter your choice: ")

   
    if choice == "1":
        title = input("Job Title: ")
        company = input("Company Name: ")
        skills = set(input("Required Skills (comma separated): ").lower().split(","))
        exp = int(input("Minimum Experience (years): "))

        job = {
            "info": (title, company),  
            "skills": skills,          
            "experience": exp
        }

        jobs.append(job)
        print("✅ Job added successfully!")

    
    elif choice == "2":
        name = input("Candidate Name: ")
        user_skills = set(input("Your Skills (comma separated): ").lower().split(","))
        user_exp = int(input("Your Experience (years): "))

        resume = {
            "name": name,
            "skills": user_skills,
            "experience": user_exp
        }

        print("📄 Resume uploaded successfully!")

   
    elif choice == "3":
        if not resume:
            print("❌ Upload resume first!")
            continue

        print("\n🔍 Matching Jobs for", resume["name"])
        found = False

        for job in jobs:
            matched_skills = resume["skills"].intersection(job["skills"])

            if matched_skills and resume["experience"] >= job["experience"]:
                title, company = job["info"]
                print("\n✔ Job:", title)
                print("Company:", company)
                print("Matched Skills:", matched_skills)
                found = True

        if not found:
            print("❌ No matching jobs found")

   
    elif choice == "4":
        if not jobs:
            print("❌ No jobs available")
        else:
            print("\n📌 Available Jobs")
            for j in jobs:
                title, company = j["info"]
                print("•", title, "at", company)

    # 5️⃣ EXIT
    elif choice == "5":
        print("👋 Thank you for using Job Portal")
        break

    else:
        print("❌ Invalid choice! Try again")

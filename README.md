# 24-623-Molecular-Simulation
24-623/12-623: Molecular Simulation of Materials
Fall 2017, 12 units
Doherty Hall 1217, Monday & Wednesday, 11:30 AM–1:20 PM
Instructor: Professor Alan McGaughey Scaife Hall 414
412-268-9605
mcgaughey@cmu.edu
Office hours: Monday & Wednesday, 1:30 PM - 2:30 PM or by appointment.
Course Assistant: Alfred Liu xingyul1@andrew.cmu.edu
Office hours: TBA
I. Description, Objective, and Outcomes
At length scales on the order of atomic spacings and time scales on the order of atomic vibra- tions, continuum descriptions of material behavior (e.g., the Fourier law of conduction, the beam equations) are no longer valid. To understand material behavior at these extreme scales, theories based on quantum mechanics, condensed matter physics, and statistical mechanics are required. The resulting theoretical formulations can be complex for even the simplest of systems. At the same time, designing and performing laboratory experiments to look at the phenomena of interest in these systems can be difficult. Numerical techniques for solving the governing equations and making observations at the atomic level are thus of critical importance for understanding the be- havior of materials at the micro- and nano-scales. This area of research is of great interest in many technological applications, including the design and fabrication of electronic, optoelectronic, energy conversion, and chemical-sensing devices.
The objective of this course is to expose students to the theory and implementation of numerical techniques for modeling atomic-level behavior. The main focus will be on classical molecular dynamics (MD) and Monte Carlo (MC) simulations. Consideration will be given to heat transfer, mass transfer, fluid mechanics, mechanics, and materials science applications. The interests of the class will play a role in choosing the applications to be discussed. In the course, you will
• Compare and contrast atomistic and continuum-level modeling tools.
• Apply thermodynamics and statistical mechanics to understand the theoretical basis behind
the MD and MC techniques.
• Write MD and MC computer codes and apply them to perform and interpret computer experiments.
• Critically assess results from MD and MC simulations presented in the scientific literature in terms of technical correctness and physical relevance.
Students are expected to have taken an undergraduate thermodynamics course. Background knowl- edge in quantum mechanics, condensed matter physics, and statistical mechanics will be helpful but is not required. Computer programming is an integral part of the course but extensive previous experience is not required. Students are free to program in a language of their choice, but should note that the instructor will be of the most help with C or C++. If you need extra material on any of these topics, please speak with the instructor.
1

II. Logistics
A. Class Time
There are two one-hour and fifty-minute meetings per week (the first class is August 28th). The time will include formal lecturing, computer demonstrations, and group work. You are responsible for all material discussed in class, whether you attended or not. There will be a set of online videos that you will be required to watch. Class will not be held on November 20th.
Use of electronic devices (laptop computers, tablets, cell phones, etc.) is not permitted in lecture unless approved by the instructor. No student may record or tape any classroom activity without the express written consent of the instructor.
If you have a disability and have an accommodations letter from the Disability Resources office, please discuss your accommodations and needs with the instructor as early in the semester as pos- sible. He will work with you to ensure that accommodations are provided as appropriate. If you suspect that you may have a disability and would benefit from accommodations but are not yet registered with the Office of Disability Resources, please contact them at access@andrew.cmu.edu. In the event that such an accommodation has been arranged, the material may not be further copied, distributed, published, or otherwise used for any other purpose without the express written consent of the instructor.
B. Website
Course materials are available on Canvas.
C. Communication
The subject of any email sent to the instructor should start with “24-623:” Do not send the in- structor emails regarding homework (see below).
D. Reading Material
There is no required textbook. You will be provided with notes and papers from the literature during the semester. The following books may be useful for reference:
• Computer Simulation of Liquids, M. P. Allen and D. J. Tildesly, Oxford, 1989, ISBN 0198556454. • Understanding Molecular Simulation, 2nd Edition, D. Frenkel and B. Smit, Academic Press,
2002, ISBN 0122673514.
• The Art of Molecular Dynamics Simulation, D. C. Rapaport, Cambridge, 2004, ISBN 0521825687.
E. Grades
A: 90-100, A-: 85-89, B+: 80-84, B: 70-79, B-: 60-69, R: <60
Grading disputes will be handled by the instructor. Requests for a grade change should be made to the instructor, in writing, within one week after the graded work is returned. Your entire submis- sion will be subject to regrading. Cheating and plagiarism is unethical behavior and is not tolerated
2

in this course or at Carnegie Mellon University. The Carnegie Mellon University policy on cheating and plagiarism will be strictly followed. Students are advised to read and adhere to the policy, which can be found at http://www.cmu.edu/policies/student-and-student-life/academic-integrity.html.
(a) Homework Assignments: 70%
There are seven homework assignments of equal weight that will lead you through the development of your own MD and MC codes. There will be short writing exercises and pencil and paper prob- lems in addition to the programming requirements. Students are encouraged to work together but must submit their own work for grading. If applicable, on your submission you must indicate who you worked with. Discussion about the homework will take place on Canvas. Do not email the instructor with questions. He and the course assistant will check the board at the end of most days.
Homework is due on Thursdays at midnight and should be submitted to Canvas. Please put all files (codes and one pdf that contains all your text and figures) into one zip file with the naming scheme (lastname) HW(homework number).zip. For example, mcgaughey HW3.zip. Do not include all your raw data in your submission. The zip file should not be hundreds of MB in size.
Homework submitted by noon of the day after it is due will be penalized 25%. Homework submit- ted by midnight of the day after it is due will be penalized 50%. Homework submitted after that time will result in a grade of zero.
(b) Case Study Presentation and Report: 30%
Working in pairs, students will give a talk and prepare a report evaluating/critiquing papers from the literature and/or performing simulations of interest to them. More details will be provided later in the semester.
F. Teaching Philosophy
Students are welcome to ask questions at all times. Don’t be afraid to interrupt if a point is not clear. A statement of the instructor’s teaching philosophy is on Canvas.
G. Take Care of Yourself
Do your best to maintain a healthy lifestyle by eating well, exercising, getting enough sleep, and taking time to relax. These steps will help you to achieve your goals and to cope with stress.
All of us benefit from support during times of struggle. There are resources available on campus and an important part of the college experience is learning how to ask for help. Asking sooner rather than later is often better. If you or anyone you know experiences academic stress, difficult life events, or feelings like anxiety or depression, I strongly encourage you to seek support. CMU Counseling and Psychological Services (CaPS) is available to help. Call 412-268-2922 and visit their website at http://www.cmu.edu/counseling/. Consider reaching out to a friend, faculty, or family member you trust to assist in getting connected to the support that can help.
  3

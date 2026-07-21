# Student Workflow Instructions

## Purpose
Nbgrader + JupyterHub @ GT OSPO gives students the ability to test basic knowledge of Git, unit testing, licensing etc.. JupyterHub provides the JupyterLab interface for students to read instructional material and complete corresponding problem sets in labeled notebooks. Nbgrader extends JupyterHub's functionality by automatically distributing and grading Jupyter notebooks submitted by the student.

Naturally, Nbgrader's workflow limits testable content. Do not worry too much about scoring so long as your responses can pass test cases on your end.

---

## Quickstart

The lesson notebooks given to students should take no more than 3 hours combined assuming little prior knowledge of Git and pytest. Any interactive content in the lessons is ***strictly optional***. The problems set notebooks should take no more than 1 hour to fully complete and validate.

![Login Default View](./img/S-Login.png)

1. Login with your [assigned ID](https://gtvault.sharepoint.com/:x:/s/ospo-team-ospo-directors/IQBmzKUq3zDFRa3WDbZBqi90AX1f3b2dB091tkYbasZedrA?e=n5lB7j) at [horizons-research.cc.gatech.edu](https://horizons-research.cc.gatech.edu).

	> *First-time users* (see graphic above): Input the desired password; this will be your future password.

1. Open a terminal inside JupyterLab. 
	1. View available assignments: Run `nbgrader list` in your home directory `~`
	1. Fetch (and override existing) assignment `PS_OSPO` from course `BashMD`: Run `nbgrader fetch_assignment PS_OSPO --replace --course BashMD`
	1. Fetch (and override existing) assignment `Modules_OSPO` from course `BashMD`: Run `nbgrader fetch_assignment Modules_OSPO --replace --course BashMD`

1. Go to the `Modules_OSPO` folder; these notebooks (`L## - Topic.ipynb`) are lessons adapted from [`gt-ospo/oss-training`](https://github.com/gt-ospo/oss-training) to work with Nbgrader.
	- Read through all notebooks starting from L00. Notebooks `L## - Git Basics`, `L## - Git Workflows`, and `L## - Pytest` contain some interactive portions. Note that completing these notebooks is ***optional*** and may not feature proper questions.
	- Do *not* submit `Modules_OSPO` but feel free to validate against the test cases which should all be visible. All interactive notebooks should already have the correct answers in the solution spaces.

1. Go to the `PS_OSPO` folder; the `PS## - Topic.ipynb` files are problem set notebooks.

	![Question View](./img/S-SolutionBounds2.png)
	- Complete all sections marked with `NotImplementedError` exceptions; these are your solution spaces
	- Do not modify any other code snippets or your score for an entire assignment may be invalidated

1. `Validate` all submissions against given test cases
	
	![Validate View](./img/S-Validate.png)
	-  Use the corresponding button in the top menu bar or type `nbgrader validate` in the root directory of the course to check every notebook.
	- ![Restart Kernel](./img/S-RestartKernel.png)
	-  You can also manually validate by restarting the kernel and running from the first cell all the way to the bottom

1. Submit `PS_OSPO` using: `nbgrader submit PS_OSPO --course BashMD`. This can be done repeatedly.

1. PS_OSPO will be automatically graded on every 10th minute for a preplanned period.\*
	> \*Note that grading will be manually done for the foreseeable future

1. Once the assignment has been graded, fetch the automatically generated feedback using: `nbgrader fetch_assignment PS_OSPO --course BashMD`

> Read the `Tips` section and start from `Detailed Workflow` if you encounter issues in this section.

---

## Tips

1. Some code snippets will write to and run external files. Ensure correct output by restarting the kernel and completely running notebooks from top to bottom. Check these external files when running these notebooks. You do not need to remove these files prior to submission.

1. If a folder with the same name as the courses (`Modules_OSPO` and `PS_OSPO`) already exists in your home directory, then `fetch_assignment` will fail. If your work has been corrupted: 
	1. Make sure your existing progress is saved somewhere!
	1. Remove the folder using `rm -f ASSIGNMENT_NAME/`
	1. nbgrader fetch_assignment ASSIGNMENT_NAME --course COURSE_NAME` as shown in the instructions above

1. Most test cases are visible but some multiple choice answers are currently hidden. Be sure to run through your own code before submission!

1. Be aware of `%%bash` sections and magics `!`.
	- When asked for a bash/command line (e.g. Git commands) response, use magics `!` or alternatively `subprocess.run()` in Python cells. 
	- Do not use magics `!` or `subprocess.run()` in `%%bash` sections; these will simply expect bash commands in order.

1. Most autograded tests either use methods from `check_helper.py` or via direct assertions. Viewing it may give an idea of how hidden tests work. Do not modify this file.

---

## Detailed Workflow

The rest of this file details each individual step and alternatives for typical student usage. Up-to-date reference instructional notebooks can be found at [`gt-ospo/oss-training`](https://github.com/gt-ospo/oss-training). Reference student view problem sets can be found in [gt-ospo/oss-training-problem-sets](https://github.com/gt-ospo/oss-training-problem-sets).

![Nbgrader Workflow](./img/S-NbgraderWorkflow.png)

As for submitting and receiving feedback, students can utilize either the Nbgrader UI or a set of command line options. Both of these are described in the `GUI` and `CLI` sections. The whole workflow encompasses the following:

1. List all available assignments (above)
1. Fetch the assignment (above)
1. Complete the assignment by filling in unimplemented sections
1. Validate the assignment
1. Submit the assignment
1. *Manually* fetch feedback from the assignment once graded

---

![Login Default View](./img/S-Login.png)

To get into your JupyterHub account, you should visit the login screen at [horizons-research.cc.gatech.edu](https://horizons-research.cc.gatech.edu). Login with your assigned username. 
- *First-time* Users: Input the desired password; this will become your future password.
- *Returning* Users: Input previous password; the account can be reset by an administrator if forgotten

Once you login, open a new terminal instance in the main panel.

![Nbgrader List](./img/S-NbgraderList.png)

Run `nbgrader list` to show all released assignments. These include assignments `Modules_OSPO` and `PS_OSPO`, both from a course called `BashMD`. To retrieve these assignments run the following in your terminal from your home (`~`) directory:
- `nbgrader fetch_assignment Modules_OSPO --course BashMD --replace`
- `nbgrader fetch_assignment PS_OSPO --course BashMD --replace`

The `Modules_OSPO` assignment/folder contains lesson content; it is recommended that students at least skim through all notebooks sequentially. The notebooks are Nbgrader adapted versions of the notebooks from [`gt-ospo/oss-training`](https://github.com/gt-ospo/oss-training). Any interactive portions are ***strictly optional***. Do not submit or be concerned about scores for `Modules_OSPO` as it is strictly for reference.

![Question View](./img/S-SolutionBounds2.png)

Inside notebooks, students put their answers in `autograded answer` cells, usually marked by (multiple) `raise NotImplementedError()` exceptions. In released solutions, these cells will contain a valid *reference* answer.

![Test Case View Hidden](./img/S-HiddenTestCase.png)

![Test Case View 1](./img/S-Assertion.png)

![Test Case View 2](./img/S-AssertionHelper.png)

Be sure to complete all notebooks in `PS_OSPO` marked as `PS## - Topic.ipynb`. Nbgrader runs the entire notebook from start to finish and gives points to `autograded tests` cells (see examples above), usually marked by `# Test Cases - Hidden` or `# Test Cases` (*Note*: Though unintended, some cells may appear completely empty. Please do not delete **any** cells!). These cells pass so long as the test case runs without throwing errors. Do *not* modify the contents in `autograded tests` or the case will automatically fail integrity checks upon grading. It should be noted that each `autograded test` cell is graded on an all-or-nothing basis, regardless of the number of points assigned to it. All test cases are visible in the `Modules_OSPO` notebooks. Most, but not all test cases are visible in `PS_OSPO` notebooks. 

## Nbgrader Walkthrough

Now that you have knowledge on how to use and complete notebooks, the following section will list steps for managing assignments with Nbgrader. The following example uses assignment `PS_OSPO` from the course `BashMD`.

![Assignment List Tool](./img/S-AssignmentList.png)

1. Go to the title bar and look for the `Assignment List`* submenu in the `Nbgrader` menu. 

![Assignment List Workflow](./img/S-AssignmentListWorkflow.png)

1. Ensure that the upper bar has `BashMD` selected, then fetch the `PS_OSPO` assignment if not in `Downloaded assignments`.

1. Complete the assignment as noted in the previous section or in the `Quickstart` section

![Validate](./img/S-Validate.png)

1. Validate the assignment. Additionally, check that no cell hangs for more than 30 seconds (See kernel status, this is the default kernel timeout).

1. Submit and fetch feedback in the `Assignment List` UI. Eash submission should create a new entry under `Submitted assignments`.

> *Note: `Assignment List` only works when one course is available (e.g. `BashMD`). This should be true in all relevant use cases.

### CLI Alternative

The complete assignment workflow for students is listed below for the assignment `PS_OSPO` in the course `BashMD`. Run the following:

1. `cd ~`: Go to home directory 
1. `nbgrader list`: List all available assignments
1. `nbgrader fetch_assignment PS_OSPO --course BashMD --replace`: Fetches course content into current directory, `--replace` flag mandatory if course already pulled
1. Validate the assignment by running `nbgrader validate NOTEBOOKDIR/*` on the ***all*** notebooks in the specified directory
1. `nbgrader submit PS_OSPO --course BashMD`: Submits read-only copy to instructor
1. `nbgrader fetch_feedback PS_OSPO --course BashMD`: Retrieves most recent autograder feedback, if it exists

> Note: It is not recommended for students to use the Python API as this adds an unnecessary layer of complexity with few benefits.


## Extra Documentation
Documentation for Nbgrader can be found [here](https://nbgrader.readthedocs.io/en/stable/configuration/jupyterhub_config.html).

### Additional Information
Students can view their most recent grades inside of each individual notebook inside returned feedback or in the `Assignment List` tab.

During the duration of onboarding, there will be a background process that scores and returns feedback on the most recent submission of `PS_OSPO`. In the output of each test case, expect a brief non-specific one-liner detailing the problem if one exists. This process runs every 5 to 15 minutes.

Calling `fetch_assignment` on an already downloaded assignment will throw an error. Either use the `-f` parameter or remove the assignment folder using `rm -r ASSIGNMENTNAME` and refetch using `nbgrader fetch_assignment ASSIGNMENT_NAME --course COURSE_NAME`. In general, not using `-f` will throw an error if overwriting existing files or folders.

### Optional Configuration

For the version of `PS01 - Git.ipynb` in `PS_OSPO` prior to 06/21/2026, you must have Git SSH properly set up with your personal GitHub account. Run the following commands inside a terminal in your JupyterHub account ***if*** there does not exist a previous SSH key; otherwise, reference the [official documentation](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys):

1. `ssh-keygen -t ed25519 -C "YOUREMAILADDRESS"`
1. `eval "$(ssh-agent -s)"`
1. `ssh-add ~/.ssh/id_ed25519` (Note: key uses default name)
1. Add ssh key in specified file to GitHub: `cat ~/.ssh/id_ed25519.pub`
1. Test the connection: `ssh -T git@github.com`

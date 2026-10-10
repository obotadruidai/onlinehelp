---
title: "Setting Up AI Center"
---

<a id="SettingUpAICenter"></a>


<a id="Prerequisites"></a>

## Prerequisites

- You need UiPath Orchestrator.
- You need to have the UiPath Assistant. For more information, see [UiPath documentation](https://docs.uipath.com/robot/docs/uipath-assistant).
- Download the [MrzDetect.zip](https://druiddocs.file.core.windows.net/docs-shares/CristinaHR/MrzDetect.zip?st=2021-02-14T07%3A39%3A30Z&se=2021-12-31T07%3A39%3A00Z&sp=rl&sv=2018-03-28&sr=f&sig=cS8ta6F4RpMGeHQ3sm0H%2F3soI0oB7tVp28k2CHKYfRU%3D) file.
- Download the [ocr-id-v2.0.zip](https://druiddocs.file.core.windows.net/docs-shares/CristinaHR/ocr-id-v2.0.zip?st=2021-02-14T07%3A39%3A56Z&se=2021-12-31T07%3A39%3A00Z&sp=rl&sv=2018-03-28&sr=f&sig=ivsItZ%2F5rR81w58zgcvdydQkXfCyUkaQx9J83Wyufw4%3D) file (OCR-IdentityCard Process) and unzip it.

To set up AI Center for Druid, follow these steps:

<a id="Step1SetUpUiPathAICenter"></a>

## Step 1: Set Up UiPath AI Center

1. Go to your Orchestrator tenant, on the main menu click **AI Center** and click the **Create Project** button.

![](../../../Resources/Images/AI%20Center/AI%20Center_41.png)

The Create new project page appears.

2. Give your project a name and a description and click **Create**.

![](../../../Resources/Images/AI%20Center/AI%20Center_42.png)

3. On the project main menu, click **ML Packages**. The packages page appears.

![](../../../Resources/Images/AI%20Center/AI%20Center_43.png)

4. Click **Upload zip file**. The Create new package page appears.
5. Enter a **Package name** and in the **Upload package** field, select the **MRZDetect.zip** file you downloaded in the Prerequisites.
6. From the **Input type** field, select **file**, and in the **Output description** field, enter **json**.

![](../../../Resources/Images/AI%20Center/AI%20Center_44.png)

7. Click **Create**. The package newly created appears in the ML Packages page and has the status "deployed".

![](../../../Resources/Images/AI%20Center/AI%20Center_45.png)

8. From the main menu, click **ML Skills** and create a new skill.
9. Choose the package previously uploaded.

![](../../../Resources/Images/AI%20Center/AI%20Center_46.png)

10. Click **Create**. The skill appears in the ML Skills page and has the status “available”.

![](../../../Resources/Images/AI%20Center/AI%20Center_47.png)

<a id="Step2SetUpUiPathprocessesforAICenter"></a>

## Step 2: Set Up UiPath processes for AI Center

1. Log in to your [orchestrator account](https://cloud.uipath.com/).
2. Download the UiPath Studio.
   ![](../../../Resources/Images/AI%20Center/AI%20Center_48.png)
3. Install UiPath on your computer.
4. Click on the desired tenant (in our example, SetupTenant).

![](../../../Resources/Images/AI%20Center/AI%20Center_49.png)

5. Go to Tenant, click **Machines** and then click **Add**.

![](../../../Resources/Images/AI%20Center/AI%20Center_50.png)

6. Click **Add Machine Template**.

![](../../../Resources/Images/AI%20Center/AI%20Center_51.png)

7. <a id="step7"></a>Enter a **Template name**, **Description** and a **License - Unattended Runtimes**.

![](../../../Resources/Images/AI%20Center/AI%20Center_52.png)

8. Click **PROVISION**.
9. <a id="step9"></a>Click **Copy Machine Key to Clipboard**.

![](../../../Resources/Images/AI%20Center/AI%20Center_53.png)

10. <a id="step10"></a>Copy the extended URL, you will need it later. In our example, *https://cloud.uipath.com/Druidsoft1/SetupTenant/*.
11. Open the UiPath Assistant app.
12. Click on **Preferences**.

![](../../../Resources/Images/AI%20Center/AI%20Center_54.png)

13. Click **Orchestrator Settings** and from the **Connection Type** drop-down, select **Machine Key**. The system automatically fills in the **Machine Name** field.

![](../../../Resources/Images/AI%20Center/AI%20Center_55.png)

14. Paste the Machine Key (from [step 9](#step9)) and Orchestrator URL (from [step 10](#step10)) and click **Connect**.
15. Go to Tenant, click **Users** and search for your email address.

![](../../../Resources/Images/AI%20Center/AI%20Center_57.png)

16. Click the three dots on the right of your email address and click **Edit**.
17. Go to the Unattended Robot section and tap on **Automatically create an unattended robot for this user**.

![](../../../Resources/Images/AI%20Center/AI%20Center_58.png)

18. Open the command prompt app and type in **whoami**. Copy the answer.

![](../../../Resources/Images/AI%20Center/AI%20Center_59.png)

19. In the **Domain\Username** field, paste the answer from the command prompt app.

![](../../../Resources/Images/AI%20Center/AI%20Center_60.png)

20. In the **Password** field, enter the password of the Windows account you use to log in on this machine and click **UPDATE**.
    You successfully created a UiPath Floating Unattended Robot!
21. Go to the **Folders** tab and click **New Folder**.
    ![](../../../Resources/Images/AI%20Center/AI%20Center_61.png)
22. <a id="step22"></a>Enter a folder **Name**, **Description**, select **Modern** as **Folder type** and **Tenant package feed** as **Process packages source**.
    ![](../../../Resources/Images/AI%20Center/AI%20Center_62.png)
23. Click **CREATE**.
24. In the Tenant, click the **Folders** tab, select your folder, go to **Machine Templates** and click **Manage Machine Templates**.

![](../../../Resources/Images/AI%20Center/AI%20Center_63.png)

25. Select the Machine Template you created at [step 7](#step7) and click **UPDATE**.

![](../../../Resources/Images/AI%20Center/AI%20Center_64.png)

26. On the left side on navigation bar, click the folder created at [step 22](#step22). Click the **Queues** tab, then click **Add**.

![](../../../Resources/Images/AI%20Center/AI%20Center_65.png)

27. The Create Queue page appears.
28. Complete the required fields and click **ADD**.
    ![](../../../Resources/Images/AI%20Center/AI%20Center_66.png)
29. <a id="step29"></a>The queue appears in the Queues page. Write down the queue’s name, you need it later.
30. Open UiPath Studio.

![](../../../Resources/Images/AI%20Center/AI%20Center_67.png)

31. Click **Open a Local Project**.

![](../../../Resources/Images/AI%20Center/AI%20Center_68.png)

32. Browse to the folder where you unzipped the **ocr-id-v2.0.zip** file (in the Prerequisites), select the **project.json** file and click **Open**.

![](../../../Resources/Images/AI%20Center/AI%20Center_69.png)

33. Right click on the process name and click **Open Project Folder**.

![](../../../Resources/Images/AI%20Center/AI%20Center_70.png)

34. Open the **Framework** folder, then the **Config** folder. There are two json files.
35. Open **DruidConfig.json**. Complete all the fields as shown in the figure below.

Fill in the **username** or **email address** and the **password** for a service account who has permissions to create a flow.

![](../../../Resources/Images/AI%20Center/AI%20Center_71.png)

36. Save the file.
37. Open **UiPathConfig.json**. Enter the folder name (from [step 22](#step22)) and the queue name (from [step 29](#step29)).

![](../../../Resources/Images/AI%20Center/AI%20Center_72.png)

38. Save the file.
39. Switch to UiPath Studio and click **Publish**.

![](../../../Resources/Images/AI%20Center/AI%20Center_73.png)

The Publish Process wizard appears.

40. Click **Next**.
41. Select Publish to **Orchestrator Tenant Process Feed** and click **Publish**.
    ![](../../../Resources/Images/AI%20Center/AI%20Center_74.png)
42. In your folder, go to **Automations** > **Processes** and click **Add**.

![](../../../Resources/Images/AI%20Center/AI%20Center_75.png)

43. <a id="step43"></a>Choose the published package, enter a **Process name** and click **CREATE**.

![](../../../Resources/Images/AI%20Center/AI%20Center_76.png)

44. Go to **Automations** > **Triggers** and click **Add**.

![](../../../Resources/Images/AI%20Center/AI%20Center_77.png)

45. Click the **Queue** button. The Create Trigger page appears.
46. Enter the trigger **Name**, select the **Queue** (from [step 29](#step29)) and the Process Name (from [step 43](#step43)).

![](../../../Resources/Images/AI%20Center/AI%20Center_78.png)

47. Click **ADD**.
48. Switch to UiPath Assistant. Find the process from [step 43](#step43), click the three dots on the right and click **Install**.

![](../../../Resources/Images/AI%20Center/AI%20Center_79.png)

You can now set up AI Center in Druid.

<a id="Step3SetUpAICenterinDruid"></a>

## Step 3: Set Up AI Center in Druid

UiPath AI Center processes user files uploaded in chat. It uses Document Understanding and the extracted information is used in the conversational context. For example, the AI Agent might ask the customers to upload the latest utilities bill and their identity card to check their address. Druid also uses AI Center to process document understanding (ID cards scan).

To set up UiPath AI Center, in the Druid Portal:

1. Go to Financial Services Flows and search for the **mrz-with-ai-fabric-response** flow. Click on the flow.
2. Click the **Details** tab and write-down the FlowID.

![](../../../Resources/Images/AI%20Center/AI%20Center_80.png)

3. Search for the flow **kyc**, go to step **process-mrz** and click the edit icon.
4. In the Set Variables section, for variable **[[KYC]].ResponseFlowId** paste the FlowID copied previously.
5. On the main menu, click **Integrations** and search for **ocr-id-v2.0-ai-fabric**.
6. Click on it. The Edit Connector Action page appears.
7. Click the **Load Orchestrator Data** button and choose your **QueueName**.
8. Click **Save & Close**.

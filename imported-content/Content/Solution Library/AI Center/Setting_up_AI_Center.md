---
title: Setting Up AI Center
---

# Setting Up AI Center

### Prerequisites

* You need UiPath Orchestrator.
* You need to have the UiPath Assistant. For more information, see [UiPath documentation](https://docs.uipath.com/robot/docs/uipath-assistant).
* Download the [MrzDetect.zip](https://druiddocs.file.core.windows.net/docs-shares/CristinaHR/MrzDetect.zip?st=2022-01-18T11%3A47%3A47Z\&se=2024-01-19T11%3A47%3A00Z\&sp=rl\&sv=2018-03-28\&sr=f\&sig=qCx7kI9lBQBeK56meq8tquvU6RtYWlMO9%2BNdw5uTNhQ%3D) file.
* Download the [ocr-id-v2.0.zip](https://druiddocs.file.core.windows.net/docs-shares/CristinaHR/ocr-id-v2.0.zip?st=2022-01-18T11%3A48%3A37Z\&se=2024-01-19T11%3A48%3A00Z\&sp=rl\&sv=2018-03-28\&sr=f\&sig=ox0n5rO0M89Ehl%2FAVPz5EKiA4uaXYTYUxe8u0DUxgD0%3D) file and unzip it.

To set up AI Center for Druid, follow these steps:

### Step 1: Set Up UiPath AI Center

1. Go to your Orchestrator tenant, on the main menu click **AI Center** and click the **Create Project** button.

![](<../../../.gitbook/assets/AI Center_41.png>)

The Create new project page appears.

2. Give your project a name and a description and click **Create**.

![](<../../../.gitbook/assets/AI Center_42.png>)

3. On the project main menu, click **ML Packages**. The packages page appears.

![](<../../../.gitbook/assets/AI Center_43.png>)

4. Click **Upload zip file**. The Create new package page appears.
5. Enter a **Package name** and in the **Upload package** field, select the **MRZDetect.zip** file you downloaded in the Prerequisites.
6. From the **Input type** field, select **file**, and in the **Output description** field, enter **json**.

![](<../../../.gitbook/assets/AI Center_44.png>)

7. Click **Create**. The package newly created appears in the ML Packages page and has the status "deployed".

![](<../../../.gitbook/assets/AI Center_45.png>)

8. From the main menu, click **ML Skills** and create a new skill.
9. Choose the package previously uploaded.

![](<../../../.gitbook/assets/AI Center_46.png>)

10. Click **Create**. The skill appears in the ML Skills page and has the status “available”.

![](<../../../.gitbook/assets/AI Center_47.png>)

### Step 2: Set Up UiPath processes for AI Center

1. Log in to your [orchestrator account](https://cloud.uipath.com/).
2. Download the UiPath Studio. ![](<../../../.gitbook/assets/AI Center_48.png>)
3. Install UiPath on your computer.
4. Click on the desired tenant (in our example, SetupTenant).

![](<../../../.gitbook/assets/AI Center_49.png>)

5. Go to Tenant, click **Machines** and then click **Add**.

![](<../../../.gitbook/assets/AI Center_50.png>)

6. Click **Add Machine Template**.

![](<../../../.gitbook/assets/AI Center_51.png>)

7. Enter a **Template name**, **Description** and a **License - Unattended Runtimes**.

![](<../../../.gitbook/assets/AI Center_52.png>)

8. Click **PROVISION**.
9. Click **Copy Machine Key to Clipboard**.

![](<../../../.gitbook/assets/AI Center_53.png>)

10. Copy the extended URL, you will need it later. In our example, _https://cloud.uipath.com/Druidsoft1/SetupTenant/_.
11. Open the UiPath Assistant app.
12. Click on **Preferences**.

![](<../../../.gitbook/assets/AI Center_54.png>)

13. Click **Orchestrator Settings** and from the **Connection Type** drop-down, select **Machine Key**. The system automatically fills in the **Machine Name** field.

![](<../../../.gitbook/assets/AI Center_55.png>)

14. Paste the Machine Key (from [step 9](Setting_up_AI_Center.md#step9)) and Orchestrator URL (from [step 10](Setting_up_AI_Center.md#step10)) and click **Connect**.
15. Go to Tenant, click **Users** and search for your email address.

![](<../../../.gitbook/assets/AI Center_57.png>)

16. Click the three dots on the right of your email address and click **Edit**.
17. Go to the Unattended Robot section and tap on **Automatically create an unattended robot for this user**.

![](<../../../.gitbook/assets/AI Center_58.png>)

18. Open the command prompt app and type in **whoami**. Copy the answer.

![](<../../../.gitbook/assets/AI Center_59.png>)

19. In the **Domain\Username** field, paste the answer from the command prompt app.

![](<../../../.gitbook/assets/AI Center_60.png>)

20. In the **Password** field, enter the password of the Windows account you use to log in on this machine and click **UPDATE**. You successfully created a UiPath Floating Unattended Robot!
21. Go to the **Folders** tab and click **New Folder**. ![](<../../../.gitbook/assets/AI Center_61.png>)
22. Enter a folder **Name**, **Description**, select **Modern** as **Folder type** and **Tenant package feed** as **Process packages source**. ![](<../../../.gitbook/assets/AI Center_62.png>)
23. Click **CREATE**.
24. In the Tenant, click the **Folders** tab, select your folder, go to **Machine Templates** and click **Manage Machine Templates**.

![](<../../../.gitbook/assets/AI Center_63.png>)

25. Select the Machine Template you created at [step 7](Setting_up_AI_Center.md#step7) and click **UPDATE**.

![](<../../../.gitbook/assets/AI Center_64.png>)

26. On the left side on navigation bar, click the folder created at [step 22](Setting_up_AI_Center.md#step22). Click the **Queues** tab, then click **Add**.

![](<../../../.gitbook/assets/AI Center_65.png>)

27. The Create Queue page appears.
28. Complete the required fields and click **ADD**. ![](<../../../.gitbook/assets/AI Center_66.png>)
29. The queue appears in the Queues page. Write down the queue’s name, you need it later.
30. Open UiPath Studio.

![](<../../../.gitbook/assets/AI Center_67.png>)

31. Click **Open a Local Project**.

![](<../../../.gitbook/assets/AI Center_68.png>)

32. Browse to the folder where you unzipped the **ocr-id-v2.0.zip** file (in the Prerequisites), select the **project.json** file and click **Open**.

![](<../../../.gitbook/assets/AI Center_69.png>)

33. Right click on the process name and click **Open Project Folder**.

![](<../../../.gitbook/assets/AI Center_70.png>)

34. Open the **Framework** folder, then the **Config** folder. There are two json files.
35. Open **DruidConfig.json**. Complete all the fields as shown in the figure below.

Fill in the **username** or **email address** and the **password** for a service account who has permissions to create a flow.

![](<../../../.gitbook/assets/AI Center_71.png>)

36. Save the file.
37. Open **UiPathConfig.json**. Enter the folder name (from [step 22](Setting_up_AI_Center.md#step22)) and the queue name (from [step 29](Setting_up_AI_Center.md#step29)).

![](<../../../.gitbook/assets/AI Center_72.png>)

38. Save the file.
39. Switch to UiPath Studio and click **Publish**.

![](<../../../.gitbook/assets/AI Center_73.png>)

The Publish Process wizard appears.

40. Click **Next**
41. Select Publish to **Orchestrator Tenant Process Feed** and click **Publish**. ![](<../../../.gitbook/assets/AI Center_74.png>)
42. In your folder, go to **Automations** > **Processes** and click **Add**.

![](<../../../.gitbook/assets/AI Center_75.png>)

43. Choose the published package, enter a **Process name** and click **CREATE**.

![](<../../../.gitbook/assets/AI Center_76.png>)

44. Go to **Automations** > **Triggers** and click **Add**.

![](<../../../.gitbook/assets/AI Center_77.png>)

45. Click the **Queue** button. The Create Trigger page appears.
46. Enter the trigger **Name**, select the **Queue** (from [step 29](Setting_up_AI_Center.md#step29)) and the Process Name (from [step 43](Setting_up_AI_Center.md#step43)).

![](<../../../.gitbook/assets/AI Center_78.png>)

47. Click **ADD**.
48. Switch to UiPath Assistant. Find the process from [step 43](Setting_up_AI_Center.md#step43), click the three dots on the right and click **Install**.

![](<../../../.gitbook/assets/AI Center_79.png>)

You can now set up AI Center in Druid.

### Step 3: Set Up AI Center in Druid

UiPath AI Center processes user files uploaded in chat. It uses Document Understanding and the extracted information is used in the conversational context. For example, the AI Agent might ask the customers to upload the latest utilities bill and their identity card to check their address. Druid also uses AI Center to process image files (ID cards scan).

To set up UiPath AI Center, in the Druid Portal:

1. Go to UiPathAiFabric Flows and click on the flow **ocr-identitycard-using-AiCenter**.
2. Click the **Details** tab, click the G**eneral** section header and write-down the **FlowID**.
3. Click the **Steps** tab, go to step **process-mrz** and click the edit icon.
4. In the Set Variables section, for variable **\[\[Account]].ResponseFlowId** paste the FlowID copied previously.
5. Click **Save**.
6. On the main menu, click **Integrations** and search for **uipath-ai-fabric-ocr-id**.
7. Click on it. The Edit Connector Action page appears on the **ConnectorSteps** tab.
8. Click to edit the only connector step available (that is, **uipath-ai-fabric-ocr-id**).

![](<../../../.gitbook/assets/ai fabric.png>)

9. Click the **Load Orchestrator Data** button and choose your **QueueName**.
10. Click **Save & Close**.

Examining the Web Stack Outage: Lessons Learned from the Recent Downtime.

Issue Summary

Duration
Start Time: January 20, 2024, 16:30 GMT
End Time: January 20, 2024, 19:45 GMT

Impact
The main web application experienced a setback during the outage, leading to a complete service interruption for 30% of our users. Users faced slow loading times, and essential features were inaccessible throughout the incident.

Timeline
Time of Detection: January 20, 2024, 16:30 UTC
Discovery Method: An automated monitoring alert was triggered due to a sudden increase in error rates and response times.

Steps Taken
Examined database servers for potential issues.
Investigated network latency as a potential culprit and checked connectivity.
Explored recent code deployments for bugs or misconfigurations.

Detours
Initially focused on frontend issues, leading to unnecessary time spent on unrelated code.
Investigated third-party services unrelated to the problem.

Escalation
Passed the incident to the DevOps and Database teams after the initial investigation.
Collaborated with senior engineers to pinpoint the root cause.

Resolution
Identified a database connection bottleneck causing increased query response times.
Implemented an emergency fix to optimise database queries and connections.
Conducted rolling restarts of affected servers to apply the fix without disrupting all users simultaneously.

Root Cause and Resolution

Root Cause
The origin of the issue was pinpointed to an abrupt surge in database traffic, resulting in heightened response times and a bottleneck in connection availability. This surge was triggered by a misconfiguration in the recent update to the database server.

Resolution
To address the issue promptly, database queries were optimised, and connection limits were increased. Additionally, a rollback to the previous version of the database server was executed to stabilise the system while a more comprehensive solution was devised.

Corrective and Preventative Measures
Enhancements
Improve monitoring alerts to offer more detailed information during anomalies.
Establish a more rigorous code review process for changes related to the database.
Conduct regular load testing to identify potential bottlenecks before they have a production impact.

Tasks
Patch Database Server:
- Apply essential updates and patches to the database server software to prevent similar misconfigurations.

Enhance Monitoring:
- Implement additional monitoring checks to promptly detect database performance issues.
- Set up alerts for abnormal query patterns and spikes in connections.

Code Review Process:
- Fortify the code review process, especially for changes involving database interactions.
- Introduce mandatory peer reviews for all modifications to the database schema.

Load Testing:
- Regularly conduct load testing to simulate high-traffic scenarios and identify potential bottlenecks before they impact production.

Documentation Update:
- Thoroughly document the incident and its resolution for future reference.

Knowledge Sharing:
- Share lessons learned with the development and operations teams through internal knowledge-sharing sessions.

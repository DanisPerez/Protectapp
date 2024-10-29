// src/components/MainContent.js
import React from 'react';
import ContentHeader from './ContentHeader';
import SummarySection from './SummarySection';
import DeviceActivityTable from './DeviceActivityTable';

const MainContent = () => {
    return (
        <div className="main-content">
        <ContentHeader />
        <SummarySection />
        <DeviceActivityTable />
        </div>
    );
};

export default MainContent;
